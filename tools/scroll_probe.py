"""Харнесс перевірки скрол-анімації.

Вбудована панель предпросмотра і фонова вкладка Chrome не композитять:
requestAnimationFrame у них видає 0 кадрів, тому анімацію там не перевірити.
Playwright-Chromium у headless дає стабільні ~60 fps і реальні події колеса.

    python tools/scroll_probe.py            # обидва замiри
    python tools/scroll_probe.py film        # тільки плівка
    python tools/scroll_probe.py wheel       # тільки порівняння колеса

ВАЖЛИВО: headless малює через SwiftShader, тобто програмно, без відеокарти.
Тому звідси МОЖНА брати геометрію, каскад і плавність потоку значень,
і НЕ МОЖНА брати fps та кількість просілих кадрів — для сторінки з
backdrop-filter це найгірший випадок і цифри будуть завищені.
"""

import io
import statistics as st
import sys

from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

URL = "http://localhost:3000/index.html"
VIEWPORT = {"width": 1920, "height": 911}
DECK_START = 2500          # scrollY, на якому починається стос карток
CARDS = "#stats .stat-card"
OUT = "stack_filmstrip.png"

# Масштаб картки з computed transform: matrix(scale, ...)
SCALES = r"""() => [...document.querySelectorAll('%s')]
    .map(c => (getComputedStyle(c).transform.match(/matrix\(([\d.]+)/) || [0, '1'])[1])
    .map(v => (+v).toFixed(3))""" % CARDS

SAMPLER = r"""() => {
  window.__tr = [];
  const card = document.querySelector('%s');
  const t0 = performance.now();
  const tick = () => {
    const m = getComputedStyle(card).transform.match(/matrix\(([\d.]+)/);
    window.__tr.push([+(performance.now() - t0).toFixed(1),
                      +window.scrollY.toFixed(1),
                      m ? +m[1] : 1]);
    window.__id = requestAnimationFrame(tick);
  };
  window.__id = requestAnimationFrame(tick);
}""" % CARDS


def open_page(pw):
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page(viewport=VIEWPORT)
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(800)
    return browser, page


def wheel_run(page, label, steps=8, delta=100, pause=110):
    """Крутить колесо дискретними щигликами і рахує роздільність руху."""
    page.evaluate(f"() => window.scrollTo(0, {DECK_START - 100})")
    page.wait_for_timeout(500)
    page.evaluate(SAMPLER)
    for _ in range(steps):
        page.mouse.wheel(0, delta)
        page.wait_for_timeout(pause)
    page.wait_for_timeout(900)                      # даємо інерції догаснути
    trace = page.evaluate("() => { cancelAnimationFrame(window.__id); return window.__tr; }")

    ys = [row[1] for row in trace]
    deltas = [ys[i] - ys[i - 1] for i in range(1, len(ys))]
    moving = [d for d in deltas if d > 0.01]

    print(f"\n--- {label} ---")
    print(f"  proideno px      : {ys[-1] - ys[0]:.0f}")
    print(f"  kadriv z ruhom   : {len(moving)} z {len(deltas)}")
    print(f"  krok/kadr mediana: {st.median(moving) if moving else 0:.2f} px")
    print(f"  krok/kadr max    : {max(moving) if moving else 0:.2f} px  (menshe = plavnishe)")
    print(f"  masshtab kartky  : {trace[0][2]:.4f} -> {trace[-1][2]:.4f}")
    return moving


def filmstrip(page, cols=3, rows=2, tile_w=620, wheel_per_frame=12):
    # 12 щигликів ≈ 1200px ≈ один --card-span, тобто кадр на картку
    """Знімає плівку прокрутки стосу — щоб анімацію можна було побачити очима."""
    shots = []
    page.evaluate(f"() => window.scrollTo(0, {DECK_START})")
    page.wait_for_timeout(700)

    for _ in range(cols * rows):
        y = page.evaluate("() => Math.round(window.scrollY)")
        shots.append((Image.open(io.BytesIO(page.screenshot())),
                      y, " ".join(page.evaluate(SCALES))))
        for _ in range(wheel_per_frame):
            page.mouse.wheel(0, 100)
            page.wait_for_timeout(90)
        page.wait_for_timeout(500)

    tile_h = int(shots[0][0].height * tile_w / shots[0][0].width)
    sheet = Image.new("RGB", (cols * tile_w, rows * (tile_h + 26)), "#111")
    draw = ImageDraw.Draw(sheet)
    for i, (img, y, scales) in enumerate(shots):
        x, top = (i % cols) * tile_w, (i // cols) * (tile_h + 26)
        sheet.paste(img.resize((tile_w, tile_h), Image.LANCZOS), (x, top))
        draw.text((x + 8, top + tile_h + 7), f"scrollY={y}   scale: {scales}", fill="#8fe07a")
    sheet.save(OUT)
    print(f"\nplivka -> {OUT}  {sheet.size}")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    with sync_playwright() as pw:
        browser, page = open_page(pw)

        fps = page.evaluate("""() => new Promise(res => {
          let n = 0; const t0 = performance.now();
          const loop = () => { n++; performance.now() - t0 < 1000 ? requestAnimationFrame(loop) : res(n); };
          requestAnimationFrame(loop);
        })""")
        print(f"rAF: {fps} fps   (0 = brauzer ne kompozytyt, zamiry nediysni)")

        if mode in ("all", "wheel"):
            wheel_run(page, "Z LENIS (yak zaraz)")
            page.evaluate("() => window.lenis && window.lenis.destroy()")
            page.wait_for_timeout(300)
            wheel_run(page, "BEZ LENIS (natyvne koleso)")
            page.reload(wait_until="networkidle")
            page.wait_for_timeout(600)

        if mode in ("all", "film"):
            filmstrip(page)

        browser.close()


if __name__ == "__main__":
    main()
