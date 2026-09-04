# ТЕХНІЧНЕ ЗАВДАННЯ (ТЗ) ДЛЯ CLAUDE: ОНОВЛЕННЯ ЕКРАНА 2 «МАНІФЕСТ» (MANDRA INVEST)

## 📌 Ціль завдання
Оновити секцію **Екрана 2 (Маніфест / Про Mandra Invest)** у файлі `site/index.html` відповідно до нового референсу та правок замовника:
1. **Зробити заголовок зеленим** — фірмовий акцентний колір `#81B873` (Unbounded, 800 bold).
2. **Зробити основний текст чистим білим** (`#FFFFFF` замість тьмяного напівпрозорого) та **трохи збільшити шрифт**.
3. **Розгорнути текст по всій ширині** (прибрати вузьке обмеження `max-width: 72ch`).
4. **Зробити дві маленькі фото-капсули світлими та яскравими**:
   * Прибрати CSS-фільтр затемнення `filter: brightness(0.58)`.
   * Згенерувати нові світлі сонячні кадри через MCP Higgsfield (детальні промпти наведені нижче).
5. Зберегти повну двомовність `[ 🌐 UA | EN ]` та перевірити результат через локальний сервер `http://localhost:3000/`.

---

## 🖼️ 1. Аналіз поточного стану та проблеми (по скріншоту)
* **Що зараз:**
  * Заголовок розбитий навпіл: перша частина біла, друга зелена.
  * Текст сірий та тьмяний (`rgba(255, 255, 255, 0.72)`).
  * Текст затиснутий у вузьку колонку по центру.
  * Дві овальні капсули-фотографії всередині тексту дуже темні, злилися з чорним фоном через `filter: brightness(0.58)`.
* **Як має бути за ТЗ:**
  * Заголовок — повністю виразний фірмовий зелений `#81B873`.
  * Тіло тексту — благородний яскравий білий `#FFFFFF` із гарною читабельністю та збільшеним кеглем.
  * Блок тексту розгорнутий широкою монументальною смугою по всій ширині контейнера (`max-width: 92vw` / `100%`).
  * Фото-капсули — яскраві, денні, з сонячним карпатським світлом та тонкою скляною рамкою `border: 1px solid rgba(255, 255, 255, 0.22)`.

---

## 🎨 2. Промпти для генерації 2 світлих фото через MCP Higgsfield

Дві маленькі фото-капсули вбудовані безпосередньо в текст:
1. **Капсула 1 (`#mfCap1`)** — стоїть у заголовку між словами «до працюючого» та «готельного продукту». Показує стильне A-frame шале Mandra в Карпатах.
2. **Капсула 2 (`#mfCap3`)** — стоїть у тексті після «у сфері гостинності». Показує мальовничу природу курорту, басейн або панораму смерек.

### 🔹 Промпт для Капсули 1 (A-frame Chalet — світле та сонячне):
```text
Bright architectural daylight photography of modern luxury A-frame wooden chalet Mandra in Ukrainian Carpathian mountains. Sun-drenched morning golden sunlight, warm natural glow, clear sky, lush green pine forest, outdoor wooden terrace with steaming hot tub, modern minimalist Scandinavian design, clean glass reflections, bright airy atmosphere, high dynamic range, photorealistic 8k, vivid natural colors, Hasselblad medium format look --ar 16:9
```
* **Параметри MCP Higgsfield (`generate_image_seedream` або `generate_image_reve`):**
  * `aspect_ratio`: `"16:9"`
  * `resolution`: `"1080p"`

### 🔹 Промпт для Капсули 2 (Resort & Nature — світле карпатське сонце):
```text
Bright daylight landscape of luxury Carpathian eco-resort nestled among tall emerald evergreen pine trees. Vibrant sunlit morning panorama, crystal clear mountain air, modern glass cottages, sparkling warm heated outdoor pool, golden sunbeams cutting through trees, bright open sky, luxury retreat vibe, ultra-sharp details, 8k resolution, authentic Ukrainian Carpathian nature --ar 16:9
```
* **Зберегти отримані зображення як:**
  * `site/assets/manifesto/cap1.webp` (або `cap1_light.webp`)
  * `site/assets/manifesto/cap3.webp` (або `cap3_light.webp`)

---

## 💻 3. Точні зміни в коді `site/index.html`

### А. HTML-розмітка секції (`#about` / `.section-manifesto`):
```html
<!-- ============================================================
     ЕКРАН 2 — МАНІФЕСТ «ПРО MANDRA INVEST»
     Широкий монументальний блок: зелений заголовок, білий збільшений текст
     ============================================================ -->
<section id="about" class="section-manifesto">
  <div class="manifesto-container">

    <!-- Бейдж секції -->
    <div class="section-badge" id="mfBadge">[ ПРО MANDRA INVEST ]</div>

    <div class="manifesto-content-wrap">
      <!-- 1. ЗАГОЛОВОК (ЗЕЛЕНИЙ #81B873) -->
      <h2 class="manifesto-title-green">
        <span id="mfTitlePart1">Від ідеї — до працюючого</span>
        <span class="inline-capsule" data-tooltip="A-frame шале Mandra" id="mfCap1">
          <img src="assets/manifesto/cap1.webp" alt="A-frame шале Mandra" decoding="async" loading="lazy">
        </span>
        <span id="mfTitlePart2">готельного продукту.</span>
      </h2>

      <!-- 2. ОСНОВНИЙ ТЕКСТ (ЧИСТИЙ БІЛИЙ #FFFFFF, ЗБІЛЬШЕНИЙ, ПО ВСІЙ ШИРИНІ) -->
      <p class="manifesto-text-white">
        <span id="mfBodyPart1">Mandra Invest — відділ продажу дохідних готельних проєктів девелопера Mandra Moments. Ми представляємо інвестиційні проєкти у сфері гостинності</span>
        <span class="inline-capsule" data-tooltip="Курорт та Карпати" id="mfCap3">
          <img src="assets/manifesto/cap3.webp" alt="Природа Карпат" decoding="async" loading="lazy">
        </span>
        <span id="mfBodyPart2">та супроводжуємо інвестора на всіх етапах — від вибору об'єкта та ознайомлення з фінансовою моделлю до придбання нерухомості.</span>
      </p>
    </div>

  </div>
</section>
```

---

### Б. CSS-стилі для вставки / заміни в `<style>`:
```css
/* ============================================================
   ЕКРАН 2 — МАНІФЕСТ «ПРО MANDRA INVEST» (ОНОВЛЕНО)
   Зелений заголовок, білий текст, світлі капсули, максимальна ширина
   ============================================================ */

.section-manifesto {
  background: var(--bg-dark); /* #121212 */
  min-height: 56vh;
  display: flex;
  align-items: center;
  padding: 6vw 4vw 5vw;
  box-sizing: border-box;
  width: 100%;
}

.manifesto-container {
  width: 100%;
  max-width: 1680px; /* Широкий розмах по всій ширині */
  margin: 0 auto;
  padding: 0 1vw;
  box-sizing: border-box;
}

.manifesto-content-wrap {
  width: 100%;
  max-width: 100%;
}

/* 1. Бейдж [ ПРО MANDRA INVEST ] */
.section-badge {
  font-family: var(--sub-font); /* 'Manrope' */
  font-size: clamp(0.85rem, 0.95vw, 1.15rem);
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #81B873; /* Фірмовий зелений */
  margin-bottom: 2vw;
}

/* 2. Заголовок — ПОВНІСТЮ ЗЕЛЕНИЙ (#81B873) */
.manifesto-title-green {
  font-family: var(--title-font); /* 'Unbounded' */
  font-size: clamp(1.9rem, 2.75vw, 3.6rem);
  font-weight: 800;
  line-height: 1.35;
  letter-spacing: -0.02em;
  color: #81B873; /* ПОВНІСТЮ ЗЕЛЕНИЙ */
  margin: 0 0 2.2vw 0;
  max-width: 100%;
}

/* 3. Основний текст — ЧИСТИЙ БІЛИЙ (#FFFFFF), ЗБІЛЬШЕНИЙ, НА ВСЮ ШИРИНУ */
.manifesto-text-white {
  font-family: var(--sub-font); /* 'Manrope' */
  font-size: clamp(1.18rem, 1.55vw, 1.95rem); /* Збільшено шрифт */
  font-weight: 400;
  line-height: 1.78;
  letter-spacing: -0.01em;
  color: #FFFFFF; /* ЧИСТИЙ БІЛИЙ замість rgba 0.72 */
  margin: 0;
  max-width: 100%; /* Прибрано обмеження 72ch — розгорнуто по ширині */
}

/* 4. Світлі капсули з фото */
.inline-capsule {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  vertical-align: middle;
  width: clamp(80px, 8.8vw, 150px);
  height: clamp(38px, 4.2vw, 70px);
  margin: 0 0.55vw;
  transform: translateY(-0.18vw);
  border-radius: 999px;
  overflow: hidden;
  position: relative;
  border: 1px solid rgba(255, 255, 255, 0.25); /* Тонкий скляний контур */
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.45);
  cursor: pointer;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease, border-color 0.4s ease;
}

.inline-capsule:hover {
  transform: translateY(-0.35vw) scale(1.06);
  border-color: #81B873;
  box-shadow: 0 14px 34px rgba(129, 184, 115, 0.28);
}

.inline-capsule img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  /* ВАЖЛИВО: ЖОДНИХ ЗАТЕМНЕНЬ! ФОТО ПОВИННО БУТИ СВІТЛИМ І СОКОВИТИМ */
  filter: brightness(1.02) saturate(1.1);
  transition: transform 0.55s cubic-bezier(0.16, 1, 0.3, 1);
}

.inline-capsule:hover img {
  transform: scale(1.12);
}
```

---

## 🌐 4. Оновлення словника перекладів (UA / EN)

У блоці JavaScript об'єкта `translations` оновити ключі, щоб двомовний тумблер `[ 🌐 UA | EN ]` працював бездоганно:

```javascript
// Українська версія (UA)
translations.ua.mfTitlePart1 = "Від ідеї — до працюючого";
translations.ua.mfTitlePart2 = "готельного продукту.";
translations.ua.mfBodyPart1 = "Mandra Invest — відділ продажу дохідних готельних проєктів девелопера Mandra Moments. Ми представляємо інвестиційні проєкти у сфері гостинності";
translations.ua.mfBodyPart2 = "та супроводжуємо інвестора на всіх етапах — від вибору об'єкта та ознайомлення з фінансовою моделлю до придбання нерухомості.";

// Англійська версія (EN)
translations.en.mfTitlePart1 = "From concept — to an operating";
translations.en.mfTitlePart2 = "hospitality asset.";
translations.en.mfBodyPart1 = "Mandra Invest is the sales division for high-yield hospitality developments by Mandra Moments. We represent premium investment projects in hospitality";
translations.en.mfBodyPart2 = "and guide investors through every stage — from asset selection and financial model review to property acquisition.";
```

І оновити масив оновлюваних ID у функції перемикання мови:
`'mfTitlePart1', 'mfTitlePart2', 'mfBodyPart1', 'mfBodyPart2'`

---

## ✅ 5. Чек-лист перевірки для Claude
1. **Заголовок:** Перевірити, що весь заголовок відображається зеленим кольором `#81B873`, шрифт `Unbounded`, жирний 800.
2. **Основний текст:** Перевірити, що текст білий `#FFFFFF` (100% непрозорість), шрифт збільшений, рядки не стиснуті, ширина не обмежена 72ch.
3. **Фото-капсули:**
   * Обидві фотографії повинні бути світлими, чіткими та сонячними (без затемнюючих фільтрів `brightness(0.58)`).
   * При наведенні курсору капсули акуратно піднімаються з легкою зеленою аурою `#81B873`.
4. **Адаптивність:**
   * На екранах від 1200px до 1920px текст комфортно займає ширину екрана без переломів слів.
   * На мобільних (до 768px) розмір шрифту плавно масштабується через `clamp()`.
5. **Тест:** Запустити або перевірити на `http://localhost:3000/`, зробити скріншот другого екрана через Puppeteer та підтвердити відповідність референсу.
