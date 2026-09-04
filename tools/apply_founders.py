with open('c:/nextweb/mandra/site/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS before </style>
founders_css = '''  /* ============================================================
     ЕКРАН 7 — ЗАСНОВНИКИ ТА ОБ'ЄКТИ
     Білий фон сторінки, всередині темна стильна рамка
     ============================================================ */
  .section-founders {
    background: #FFFFFF;
    padding: 0 0 140px;
    width: 100%;
    position: relative;
    box-sizing: border-box;
  }
  .founders-container {
    max-width: 1440px;
    margin: 0 auto;
    padding: 0 6vw;
  }
  .founders-frame {
    background: #0B100E;
    border: 1px solid rgba(0, 0, 0, 0.08);
    border-radius: 24px;
    padding: 22px;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.12);
    box-sizing: border-box;
  }

  /* Верхня сітка: Ліва картка + 2 картки засновників */
  .founders-top-grid {
    display: grid;
    grid-template-columns: 1.85fr 1fr 1fr;
    gap: 16px;
    align-items: stretch;
  }

  /* Ліва картка з фоном хвої та текстом */
  .founders-hero-card {
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    background-color: #121A15;
    background-image: url('assets/founders/pine_card_clean.jpg');
    background-size: cover;
    background-position: center right;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    min-height: 240px;
    padding: 34px 30px;
    box-sizing: border-box;
  }
  .founders-hero-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(7, 11, 9, 0.85) 0%, rgba(7, 11, 9, 0.45) 60%, transparent 100%);
    pointer-events: none;
    z-index: 1;
  }
  .founders-hero-text {
    position: relative;
    z-index: 2;
    font-family: var(--title-font);
    font-size: clamp(1.15rem, 1.4vw, 1.85rem);
    font-weight: 700;
    line-height: 1.35;
    letter-spacing: -0.01em;
    color: #FFFFFF;
    margin: 0;
    max-width: 480px;
    text-shadow: 0 2px 14px rgba(0, 0, 0, 0.6);
  }

  /* Картки засновників */
  .founder-profile-card {
    display: flex;
    flex-direction: column;
  }
  .founder-img-wrap {
    width: 100%;
    aspect-ratio: 1.05 / 1;
    border-radius: 14px;
    overflow: hidden;
    background: #18221C;
  }
  .founder-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .founder-profile-card:hover .founder-img {
    transform: scale(1.04);
  }
  .founder-info {
    padding-top: 12px;
  }
  .founder-name {
    font-family: var(--title-font);
    font-size: clamp(1.05rem, 1.15vw, 1.4rem);
    font-weight: 700;
    color: #FFFFFF;
    margin: 0 0 4px 0;
    letter-spacing: -0.01em;
  }
  .founder-role {
    font-family: var(--sub-font);
    font-size: clamp(0.72rem, 0.78vw, 0.9rem);
    line-height: 1.4;
    color: rgba(255, 255, 255, 0.62);
    margin: 0;
  }

  /* Нижня сітка з 6 фотографіями */
  .founders-gallery-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 12px;
    margin-top: 16px;
  }
  .founder-thumb-box {
    aspect-ratio: 1.14 / 1;
    border-radius: 12px;
    overflow: hidden;
    background: #18221C;
    cursor: pointer;
    position: relative;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease;
  }
  .founder-thumb-box:hover {
    transform: translateY(-3px) scale(1.03);
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.45);
    z-index: 2;
  }
  .founder-thumb-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  @media (max-width: 900px) {
    .section-founders { padding: 0 0 80px; }
    .founders-frame { padding: 16px; border-radius: 18px; }
    .founders-top-grid {
      grid-template-columns: 1fr;
      gap: 14px;
    }
    .founders-hero-card {
      min-height: 180px;
      padding: 24px 20px;
    }
    .founders-gallery-grid {
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
    }
  }
'''

content = content.replace('</style>', founders_css + '\n</style>', 1)

# 2. Add Screen 7 HTML after </section> of #partners
founders_html = '''
  <!-- ============================================================
       ЕКРАН 7 — ЗАСНОВНИКИ ТА ОБ'ЄКТИ
       На білому фоні сторінки, всередині темна стильна рамка
       ============================================================ -->
  <section class="section-founders" id="founders">
    <div class="founders-container">
      <div class="founders-frame">
        <!-- Верхня сітка: Хвойний блок + 2 засновники -->
        <div class="founders-top-grid">
          <!-- Лівий блок з цитатою -->
          <div class="founders-hero-card">
            <h3 class="founders-hero-text" id="foundersHeroText">
              Власний інвестиційний проєкт від засновників Mandra Moments та Ribas Hotels Group
            </h3>
          </div>

          <!-- Картка Артура Лупашка -->
          <article class="founder-profile-card">
            <div class="founder-img-wrap">
              <img src="assets/founders/artur_lupashko.jpg" alt="Артур Лупашко" class="founder-img" loading="lazy">
            </div>
            <div class="founder-info">
              <h4 class="founder-name" id="founderName1">Артур Лупашко</h4>
              <p class="founder-role" id="founderRole1">Засновник Ribas Hotels Group і співзасновник Mandra Moments</p>
            </div>
          </article>

          <!-- Картка Сергія Боєва -->
          <article class="founder-profile-card">
            <div class="founder-img-wrap">
              <img src="assets/founders/serhiy_boiev.jpg" alt="Сергій Боєв" class="founder-img" loading="lazy">
            </div>
            <div class="founder-info">
              <h4 class="founder-name" id="founderName2">Сергій Боєв</h4>
              <p class="founder-role" id="founderRole2">Співзасновник Mandra Moments</p>
            </div>
          </article>
        </div>

        <!-- Нижня сітка з 6 фотографіями реалізованих локацій -->
        <div class="founders-gallery-grid">
          <div class="founder-thumb-box" title="Mandra Glamping Interior">
            <img src="assets/founders/gallery_1.jpg" alt="Mandra Glamping Interior" class="founder-thumb-img" loading="lazy">
          </div>
          <div class="founder-thumb-box" title="Mandra Pool">
            <img src="assets/founders/gallery_2.jpg" alt="Mandra Pool" class="founder-thumb-img" loading="lazy">
          </div>
          <div class="founder-thumb-box" title="Mandra Forest Resort">
            <img src="assets/founders/gallery_3.jpg" alt="Mandra Forest Resort" class="founder-thumb-img" loading="lazy">
          </div>
          <div class="founder-thumb-box" title="Mandra Terrace">
            <img src="assets/founders/gallery_4.jpg" alt="Mandra Terrace" class="founder-thumb-img" loading="lazy">
          </div>
          <div class="founder-thumb-box" title="Mandra A-frame Chalet">
            <img src="assets/founders/gallery_5.jpg" alt="Mandra A-frame Chalet" class="founder-thumb-img" loading="lazy">
          </div>
          <div class="founder-thumb-box" title="Mandra Safari Glamping">
            <img src="assets/founders/gallery_6.jpg" alt="Mandra Safari Glamping" class="founder-thumb-img" loading="lazy">
          </div>
        </div>
      </div>
    </div>
  </section>
'''

target_tag = '</section>\n\n  <!-- Sleek Side Tab Trigger -->'
if target_tag in content:
    content = content.replace(target_tag, '</section>\n' + founders_html + '\n  <!-- Sleek Side Tab Trigger -->', 1)
else:
    print('Warning: target_tag not found!')

# 3. Add to translations
ua_old = "partnersTitle: 'Партнери Мандра Інвест'\n      },"
ua_new = '''partnersTitle: 'Партнери Мандра Інвест',
        /* ЕКРАН 7 — ЗАСНОВНИКИ */
        foundersHeroText: 'Власний інвестиційний проєкт від засновників Mandra Moments та Ribas Hotels Group',
        founderName1: 'Артур Лупашко',
        founderRole1: 'Засновник Ribas Hotels Group і співзасновник Mandra Moments',
        founderName2: 'Сергій Боєв',
        founderRole2: 'Співзасновник Mandra Moments'
      },'''
content = content.replace(ua_old, ua_new, 1)

en_old = "partnersTitle: 'Mandra Invest Partners'\n      }\n    };"
en_new = '''partnersTitle: 'Mandra Invest Partners',
        /* SCREEN 7 — FOUNDERS */
        foundersHeroText: 'Proprietary investment project from the founders of Mandra Moments & Ribas Hotels Group',
        founderName1: 'Artur Lupashko',
        founderRole1: 'Founder of Ribas Hotels Group & Co-founder of Mandra Moments',
        founderName2: 'Serhiy Boiev',
        founderRole2: 'Co-founder of Mandra Moments'
      }
    };'''
content = content.replace(en_old, en_new, 1)

# 4. Add to s2 array
s2_old = "'partnersTitle'];"
s2_new = "'partnersTitle',\n                  'foundersHeroText','founderName1','founderRole1','founderName2','founderRole2'];"
content = content.replace(s2_old, s2_new, 1)

with open('c:/nextweb/mandra/site/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('c:/nextweb/mandra/site/numo-style.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Added Screen 7 founders section successfully!')
