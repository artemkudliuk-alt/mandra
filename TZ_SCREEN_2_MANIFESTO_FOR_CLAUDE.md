# ТЕХНИЧЕСКОЕ ЗАДАНИЕ (ТЗ) ДЛЯ CLAUDE: ОБНОВЛЕНИЕ МАНІФЕСТА (ЭКРАН 2)
## Ключевые правки: Высота экрана +40%, Жирное первое предложение, Фото-капсулы увеличены в 2 раза

---

## 1. Что изменено и зафиксировано:

1. **Высота экрана увеличена на 40%:**
   * Секция получила просторный монументальный ритм: `min-height: 128vh; padding: 9vw 5vw;` (вместо прежних 92vh).
   * За счет этого текст дышит, а белый фон благородно разделяет темный Hero и нижнюю галерею.
2. **Типографический контраст:**
   * **Первое предложение:** Оставлено **ЖИРНЫМ** (`font-weight: 800; color: #0E1F0B;`):  
     `Від ідеї — до працюючого готельного продукту [КАПСУЛА 1].`
   * **Всё остальное:** Сделано **ТОНКИМ** (`font-weight: 300; color: #2D3740;`):  
     `Mandra Invest — відділ продажу дохідних готельних проєктів...`
3. **Фотографии (капсулы) увеличены ровно в 2 раза:**
   * Ширина: **`10.8vw`** (min-width: 140px) вместо 5.5vw.
   * Высота: **`5.2vw`** (min-height: 68px) вместо 2.8vw.
   * Межстрочный интервал текста: увеличен до **`line-height: 1.82`**, чтобы большие панорамные капсулы не пересекали строки.
   * Отступы: `margin: 0 0.8vw; transform: translateY(-0.25vw);`.
   * Тень: усилена до `box-shadow: 0 12px 34px rgba(0, 0, 0, 0.16);`.

---

## 2. Разметка секции в `c:\nextweb\mandra\site\index.html`:

```html
<section id="about" class="section-manifesto">
  <div class="manifesto-container">

    <div class="section-badge" id="mfBadge">[ ПРО MANDRA INVEST ]</div>

    <h2 class="manifesto-text">
      <!-- Первое предложение: ЖИРНОЕ (font-weight: 800) -->
      <span class="manifesto-lead-bold">
        <span id="mfPart1">Від ідеї — до працюючого готельного продукту</span>
        <span class="inline-capsule" data-tooltip="A-frame шале Mandra з чаном" id="mfCap1">
          <img src="assets/manifesto/cap1.jpg" alt="A-frame шале Mandra">
        </span>.
      </span>

      <!-- Все последующие предложения: ТОНКИЕ (font-weight: 300) -->
      <span class="manifesto-body-light">
        <span id="mfPart2">Mandra Invest — відділ продажу дохідних готельних проєктів девелопера Mandra Moments</span>
        <span class="inline-capsule" data-tooltip="Засновники та партнери Ribas Hotels" id="mfCap2">
          <img src="assets/manifesto/cap2.jpg" alt="Засновники та команда">
        </span>. 
        <span id="mfPart3">Ми представляємо інвестиційні проєкти у сфері гостинності</span>
        <span class="inline-capsule" data-tooltip="Карпатські смереки та природа" id="mfCap3">
          <img src="assets/manifesto/cap3.jpg" alt="Природа Карпат">
        </span> 
        <span id="mfPart4">та супроводжуємо інвестора на всіх етапах — від вибору об'єкта та ознайомлення з фінансовою моделлю до придбання нерухомості</span>
        <span class="inline-capsule" data-tooltip="Супровід інвестора та дохідність" id="mfCap4">
          <img src="assets/manifesto/cap4.jpg" alt="Інтер'єр та сервіс">
        </span>
        <span id="mfPart5">.</span>
      </span>
    </h2>

  </div>
</section>
```

---

## 3. CSS параметры:

```css
:root {
  --capsule-w: 10.8vw;
  --capsule-h: 5.2vw;
}

.section-manifesto {
  background: #FFFFFF;
  min-height: 128vh; /* Увеличено на 40% */
  display: flex;
  align-items: center;
  padding: 9vw 5vw;
}

.manifesto-text {
  font-family: var(--title-font);
  font-size: var(--s2m-text-size);
  line-height: 1.82;
  letter-spacing: -0.01em;
  margin: 0;
}

.manifesto-lead-bold {
  font-weight: 800;
  color: #0E1F0B;
}

.manifesto-body-light {
  font-weight: 300;
  color: #2D3740;
}

.inline-capsule {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  vertical-align: middle;
  width: var(--capsule-w);
  height: var(--capsule-h);
  min-width: 140px;
  min-height: 68px;
  margin: 0 0.8vw;
  transform: translateY(-0.25vw) scale(0.85);
  border-radius: 999px;
  overflow: hidden;
  position: relative;
  box-shadow: 0 12px 34px rgba(0, 0, 0, 0.16);
  cursor: pointer;
}
```

---

## 4. Результат проверки:
Изменения уже применены в файлах `c:\nextweb\mandra\site\index.html` и `numo-style.html`, проверены на локальном сервере `http://localhost:3000/`.
