# ТЕХНІЧНЕ ЗАВДАННЯ (ТЗ): СКРОЛ-ШОУКЕЙС (ЕКРАН 3) → СТАТИСТИКА (ЕКРАН 4)
## Безшовний перехід з утриманням карток по боках (15%) та напливом статистики ззаду

---

## 1. Головна кінематика та візуальна концепція:

1. **Екран 3 (`#showcase`):**
   - **Фаза 1 (Вхід):** Перша фотокартка (01 — Аналіз) відкривається на всю ширину сцени з заголовком «Ми відповідаємо за».
   - **Фаза 2 (Збірка 2x2, `p = 0 → 0.38`):** При скролі чотири квадратні фотокартки розходяться у сітку 2x2. Заголовок тане на самому початку.
   - **Фаза 3 (Пауза, `p = 0.38 → 0.50`):** Коротке плато для читання контенту всіх 4 карток.
   - **Фаза 4 (Розсування у сторони, `p = 0.50 → 1.0`):** Картки **НЕ зникають** і не відлітають у небуття:
     - Ліві картки (`01`, `03`) зсуваються вліво (`-44vw`).
     - Праві картки (`02`, `04`) зсуваються вправо (`+44vw`).
     - **По краях екрана залишається видно ~15% ширини кожної картки** з повною непрозорістю (`opacity: 1`), формуючи архітектурні бокові куліси.

2. **Екран 4 (`#stats` — «Мандра Інвест в цифрах»):**
   - **Шар розташування:** Знаходиться **ПІД** фотокартками (`z-index: 1`, тоді як шоукейс — `z-index: 3`).
   - **Ранній підйом:** Завдяки `margin-top: -65vh` та оптимізованій висоті треку (`185vh`), секція статистики починає підніматися **ОДРАЗУ, як тільки картки починають розсуватися** (`p >= 0.50`).
   - **Повна відсутність порожнього екрана:** Користувач не скролить порожнє чорне поле. Тільки-но картки розсуваються, між ними знизу плавно виринає заголовок «Мандра Інвест в цифрах» та каскадний стек карток (`42+`, `16%`, `4...`).
   - **Відсутність будь-яких швів, смуг та ліній:** Фон єдиний і монолітний (`var(--bg-dark)` / `#121212`), без верхніх тіней чи градієнтних смуг.

---

## 2. Реалізація в CSS (`site/index.html`):

```css
/* Екран 3 — Шоукейс: z-index: 3, прозорий фон */
.section-scroll-showcase {
  position: relative;
  z-index: 3;
  background: transparent;
  margin-top: -1px;
  height: 185vh; /* Оптимальна динаміка без мертвого скролу */
}

.showcase-sticky {
  position: sticky;
  top: 0;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: visible;
  padding: 9vh 3.6vw 2vh;
  background: transparent;
  pointer-events: none;
}

.showcase-card {
  position: absolute;
  overflow: hidden;
  border-radius: 20px;
  border: none;
  will-change: left, top, width, height, transform, opacity;
  pointer-events: auto;
  background: #0E1F0B;
  box-shadow: 0 22px 60px rgba(14, 31, 11, 0.22);
}

/* Екран 4 — Статистика: z-index: 1, напливає ззаду під картки */
.section-stats-stack {
  position: relative;
  z-index: 1;
  background: transparent;
  color: #FFFFFF;
  padding: 70px 6vw 80px;
  overflow: visible;
  border-top: none;
  margin-top: -65vh; /* Виринає під розсувні фотокартки */
}

@media (max-width: 900px) {
  .section-stats-stack { padding: 80px 5vw 100px; margin-top: -20vh; }
}
```

---

## 3. Реалізація в JS (`initShowcaseScrub`):

```javascript
const ASSEMBLE_END = 0.38;   /* 0 → 38%: збірка у сітку 2x2 */
const HOLD_END     = 0.50;   /* 38 → 50%: пауза 2x2 */
const FLY_VW       = 44;     /* ~15% ширини лишається видимим по боках */

function easeOutExpo(x) { return x >= 1 ? 1 : 1 - Math.pow(2, -10 * x); }
function easeInOutQuad(x) { return x < 0.5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2; }
const lerp = (a, b, t) => a + (b - a) * t;
const clamp01 = (x) => Math.max(0, Math.min(1, x));

// У функції render():
const a  = easeOutExpo(clamp01(p / ASSEMBLE_END));
const fo = easeInOutQuad(clamp01((p - HOLD_END) / (1 - HOLD_END)));

for (let i = 0; i < items.length; i++) {
  const el = items[i];
  const q  = el.dataset.q;
  const f  = FINAL[q];
  if (!f) continue;

  el.style.left   = lerp(START.l, f.l, a).toFixed(3) + '%';
  el.style.top    = lerp(START.t, f.t, a).toFixed(3) + '%';
  el.style.width  = lerp(START.w, f.w, a).toFixed(3) + '%';
  el.style.height = lerp(START.h, f.h, a).toFixed(3) + '%';

  const dir = (q === 'tl' || q === 'bl') ? -1 : 1;
  const tx  = (dir * FLY_VW * fo).toFixed(2);
  el.style.transform = 'translate3d(' + tx + 'vw,0,0)';
  el.style.opacity   = '1'; // Фотокартки лишаються чіткими по боках

  const isLead = el.classList.contains('showcase-lead');
  const badge = el.querySelector('.card-badge');
  const num   = el.querySelector('.card-index');
  const vis   = isLead ? 1 : clamp01((a - 0.3) / 0.45);
  const textOpacity = (vis * (1 - fo * 0.9)).toFixed(3);
  if (badge) badge.style.opacity = textOpacity;
  if (num)   num.style.opacity   = ((isLead ? 1 : vis) * (1 - fo * 0.9)).toFixed(3);
}

// Наплив секції статистики: плавно проявляється тільки коли картки починають розсуватися
const statsEl = document.getElementById('stats');
if (statsEl) {
  const statsOpacity = p < HOLD_END ? 0 : clamp01((p - HOLD_END) / 0.15);
  statsEl.style.opacity = statsOpacity.toFixed(3);
}
```
