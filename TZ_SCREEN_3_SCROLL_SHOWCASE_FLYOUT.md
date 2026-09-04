# ТЕХНІЧНЕ ЗАВДАННЯ (ТЗ) ДЛЯ CLAUDE: СКРОЛ-ШОУКЕЙС (ЕКРАН 3)
## Розміри карток (збільшена висота) + Розліт карток у сторони за межі екрана (Fly-Out)
### Референс механіки: https://alexvillasgroup.com/

---

## 1. Що зрозуміло по задачі:

1. **Проблема зараз:**  
   Зараз на сайті 4 картки роз'їжджаються в сітку 2x2, але після цього блок просто піднімається вгору разом зі скролом сторінки як звичайний блок. До того ж висота карток замала (`58vh` на всю сцену), вони виглядають приплюснутими.

2. **Як має працювати замовлене оновлення:**
   * **Фаза 1 (Вхід):** Секція фіксується (`position: sticky`). Спочатку показується велика картка 01 з текстом і заголовком.
   * **Фаза 2 (Роз'їзд у квадратну сітку 2x2):** При скролі 4 картки плавно розходяться у свої 4 кути — стають рівно, квадратно («рівненько, квадратненько»), красиво заповнюючи робоче вікно.
   * **Фаза 3 (Пауза для читання):** Коротке плато у скролі, де сітка 2x2 зафіксована і користувач може роздивитися контент.
   * **Фаза 4 (Розліт у сторони / Fly-Out за краї):** При продовженні скролу картки **НЕ піднімаються вгору**. Вони **роз'їжджаються в сторони за межі екрана** (ліві улітають вліво за лівий край, праві — вправо за правий край) з плавним згасанням (`opacity`). Сцена звільняється, і тільки тоді плавно відкривається наступний екран.
   * **Розміри карток:** Збільшити висоту робочого вікна `.showcase-stage` з `58vh` до **`68vh` – `72vh`**, а ширину до **`1200px` – `1260px`** (або `86vw`), щоб картки мали солідні, високі, збалансовані пропорції.

---

## 2. Зміни в CSS (`site/index.html`):

```css
/* ============================================================
   ЕКРАН 3 — СКРОЛ-ШОУКЕЙС З РОЗЛЬОТОМ У СТОРОНИ (FLY-OUT)
   ============================================================ */

.section-scroll-showcase {
  position: relative;
  background: #FFFFFF;
  margin-top: -1px;
  /* Збільшуємо довжину треку для 3 фаз (розкриття + пауза + розліт) */
  height: 230vh;
}

.showcase-sticky {
  position: sticky;
  top: 0;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden; /* Щоб картки акуратно ховалися за межами екрана */
  padding: 6vh 3vw 3vh;
  box-sizing: border-box;
}

/* ЗБІЛЬШЕННЯ РОЗМІРІВ СЦЕНИ ТА ВИСОТИ КАРТОК */
.showcase-stage {
  position: relative;
  width: 100%;
  max-width: 1240px; /* Збільшено з 1080px */
  height: 70vh;       /* Збільшено з 58vh — картки стають високими та солідними */
  margin: 0 auto;
}

.showcase-grid {
  position: absolute;
  inset: 0;
}

.showcase-card,
.showcase-lead {
  position: absolute;
  border-radius: 24px;
  overflow: hidden;
  will-change: transform, opacity, left, top, width, height;
}

.showcase-card {
  background: #0E1F0B;
  box-shadow: 0 24px 64px rgba(14, 31, 11, 0.22);
}

.showcase-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
```

---

## 3. Зміни в JavaScript (Скрол-механіка розльоту):

Замінити функцію `initShowcaseScrub` на оновлену з 3-фазною логікою:

```javascript
(function initShowcaseScrub() {
  const track = document.querySelector('.section-scroll-showcase');
  if (!track) return;
  const items = Array.from(track.querySelectorAll('[data-q]'));
  const title = track.querySelector('.showcase-title');
  if (!items.length) return;

  const GAP = 1.8;                      /* зазор між картками, % */
  const SIDE = (100 - GAP) / 2;         /* розмір картки у сітці 2x2, % */

  /* Координати сітки 2x2 */
  const GRID = {
    tl: { l: 0,          t: 0,          w: SIDE, h: SIDE, dx: -140, dy: -20 },
    tr: { l: SIDE + GAP, t: 0,          w: SIDE, h: SIDE, dx:  140, dy: -20 },
    bl: { l: 0,          t: SIDE + GAP, w: SIDE, h: SIDE, dx: -140, dy:  20 },
    br: { l: SIDE + GAP, t: SIDE + GAP, w: SIDE, h: SIDE, dx:  140, dy:  20 }
  };
  const START = { l: 0, t: 0, w: 100, h: 100 };

  const lerp = (a, b, t) => a + (b - a) * t;
  const clamp = (v, min, max) => Math.max(min, Math.min(max, v));
  const easeOutCubic = (x) => 1 - Math.pow(1 - x, 3);
  const easeInCubic  = (x) => x * x * x;

  let ticking = false;

  function render() {
    ticking = false;
    const rect = track.getBoundingClientRect();
    const total = track.offsetHeight - window.innerHeight;
    let p = total > 0 ? (-rect.top) / total : 0;
    p = clamp(p, 0, 1);

    /* -----------------------------------------------------------
       ФАЗА 1: 0.00 -> 0.42 — З'їзд / розкриття карток у сітку 2x2
       ФАЗА 2: 0.42 -> 0.62 — Пауза (зафіксована ідеальна сітка 2x2)
       ФАЗА 3: 0.62 -> 1.00 — Розліт карток у сторони за край екрана
       ----------------------------------------------------------- */

    // Прогрес першої фази (розкриття)
    const pIntro = clamp(p / 0.42, 0, 1);
    const eIntro = easeOutCubic(pIntro);

    // Прогрес третьої фази (розліт у сторони)
    const pExit = clamp((p - 0.62) / 0.38, 0, 1);
    const eExit = easeInCubic(pExit);

    // Анімація карток
    for (let i = 0; i < items.length; i++) {
      const el = items[i];
      const g = GRID[el.dataset.q];
      if (!g) continue;

      // Базове позиціонування у сітці
      const curL = lerp(START.l, g.l, eIntro);
      const curT = lerp(START.t, g.t, eIntro);
      const curW = lerp(START.w, g.w, eIntro);
      const curH = lerp(START.h, g.h, eIntro);

      el.style.left   = curL.toFixed(3) + '%';
      el.style.top    = curT.toFixed(3) + '%';
      el.style.width  = curW.toFixed(3) + '%';
      el.style.height = curH.toFixed(3) + '%';

      // Розліт у сторони на фінальному етапі
      if (pExit > 0) {
        const moveX = g.dx * eExit;
        const moveY = g.dy * eExit;
        const op = clamp(1 - (pExit * 1.3), 0, 1);
        el.style.transform = `translate3d(${moveX.toFixed(2)}vw, ${moveY.toFixed(2)}vh, 0)`;
        el.style.opacity   = op.toFixed(3);
      } else {
        el.style.transform = 'translate3d(0, 0, 0)';
        el.style.opacity   = '1';
      }

      // Поява підписів і номерів
      const isLead = el.classList.contains('showcase-lead');
      const badge = el.querySelector('.card-badge');
      const num   = el.querySelector('.card-index');
      const vis   = isLead ? 1 : clamp((eIntro - 0.25) / 0.5, 0, 1);
      if (badge) badge.style.opacity = vis.toFixed(3);
      if (num)   num.style.opacity   = (isLead ? 1 : vis).toFixed(3);
    }

    // Анімація заголовка "Ми відповідаємо за" при вильоті
    if (title) {
      if (pExit > 0) {
        title.style.opacity = clamp(1 - pExit * 1.5, 0, 1).toFixed(3);
        title.style.transform = `translateY(-${(pExit * 40).toFixed(1)}px)`;
      } else {
        title.style.opacity = '1';
        title.style.transform = 'translateY(0)';
      }
    }
  }

  function onScroll() {
    if (!ticking) { ticking = true; requestAnimationFrame(render); }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  render();
})();
```

---

## 4. Чек-лист перевірки для Claude:
1. **Висота карток:** Перевірити, що сцена займає `70vh` (висота картки ~`34vh`), вони не сплюснуті, а виглядають благородно та просторо.
2. **Зупинка в сітці 2x2:** На відрізку скролу `42% – 62%` картки стоять ідеально рівно по 4 квадрантах із чіткими зазорами.
3. **Розліт у сторони:** При подальшому скролі картки плавно розлітаються вліво та вправо за межі в'юпорту (`translate3d`), а не повзуть тупо вгору.
4. **Тест:** Протестувати на `http://localhost:3000/`, перевірити плавність 60fps при русі коліщатка миші та на тачпаді.
