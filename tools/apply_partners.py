with open('c:/nextweb/mandra/site/numo-style.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS before </style>
partners_css = '''  /* ============================================================
     ЕКРАН 6 — ПАРТНЕРИ МАНДРА ІНВЕСТ
     Білий фон, заголовок, нескінченна рухома стрічка логотипів (hover: pause + scale)
     ============================================================ */
  .section-partners {
    background: #FFFFFF;
    color: #0B110D;
    padding: 96px 0 110px;
    position: relative;
    overflow: hidden;
    width: 100%;
    border-top: 1px solid rgba(0, 0, 0, 0.06);
  }
  .partners-top-container {
    max-width: 1440px;
    margin: 0 auto;
    padding: 0 6vw 36px;
  }
  .partners-title {
    font-family: var(--title-font);
    font-size: clamp(2rem, 2.7vw, 3.6rem);
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -0.02em;
    color: #0E1611;
    margin: 0;
  }

  /* Стрічка біжучого рядка логотипів */
  .partners-marquee-wrap {
    width: 100%;
    overflow: hidden;
    position: relative;
    padding: 16px 0;
    mask-image: linear-gradient(to right, transparent 0%, black 6%, black 94%, transparent 100%);
    -webkit-mask-image: linear-gradient(to right, transparent 0%, black 6%, black 94%, transparent 100%);
  }
  .partners-marquee {
    display: flex;
    width: 100%;
    overflow: hidden;
    user-select: none;
  }
  .marquee-track {
    display: flex;
    align-items: center;
    gap: clamp(60px, 7vw, 130px);
    width: max-content;
    animation: partnersMarqueeScroll 32s linear infinite;
    will-change: transform;
    padding: 15px 0;
  }

  /* Пауза при наведенні миші на будь-яке лого чи стрічку */
  .partners-marquee:hover .marquee-track {
    animation-play-state: paused;
  }

  @keyframes partnersMarqueeScroll {
    0% { transform: translate3d(0, 0, 0); }
    100% { transform: translate3d(-33.333333%, 0, 0); }
  }

  /* Логотипи: розміри, відступи, плавний скейл при ховері */
  .partner-logo-box {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 110px;
    padding: 0 10px;
    cursor: pointer;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
    opacity: 0.88;
  }
  .partner-logo-box:hover {
    transform: scale(1.22);
    opacity: 1;
    z-index: 10;
  }

  /* Розміри логотипів: не маленькі, гармонійні пропорції */
  .partner-img {
    display: block;
    width: auto;
    object-fit: contain;
    pointer-events: none;
  }
  .partner-img.logo-mandra { height: 56px; max-width: 220px; }
  .partner-img.logo-yod { height: 48px; max-width: 180px; }
  .partner-img.logo-ekopark { height: 74px; max-width: 160px; }
  .partner-img.logo-ribas { height: 54px; max-width: 170px; }
  .partner-img.logo-happytime { height: 58px; max-width: 150px; }
  .partner-img.logo-temo { height: 38px; max-width: 260px; }

  @media (max-width: 900px) {
    .section-partners { padding: 64px 0 74px; }
    .partners-top-container { padding: 0 6vw 24px; }
    .partners-title { font-size: 7.6vw; }
    .marquee-track {
      gap: 46px;
      animation-duration: 22s;
    }
    .partner-logo-box { height: 80px; }
    .partner-img.logo-mandra { height: 42px; }
    .partner-img.logo-yod { height: 36px; }
    .partner-img.logo-ekopark { height: 56px; }
    .partner-img.logo-ribas { height: 40px; }
    .partner-img.logo-happytime { height: 44px; }
    .partner-img.logo-temo { height: 28px; }
  }
'''

content = content.replace('</style>', partners_css + '\n</style>', 1)

# 2. Add Screen 6 markup right after </section> of #petrichor
partners_html = '''
  <!-- ============================================================
       ЕКРАН 6 — ПАРТНЕРИ МАНДРА ІНВЕСТ
       Білий фон, заголовок, нескінченна рухома стрічка логотипів (hover: pause + scale)
       ============================================================ -->
  <section class="section-partners" id="partners">
    <div class="partners-top-container">
      <h2 class="partners-title" id="partnersTitle">Партнери Мандра Інвест</h2>
    </div>

    <!-- Нескінченна біжуча стрічка логотипів -->
    <div class="partners-marquee-wrap">
      <div class="partners-marquee">
        <div class="marquee-track">
          <!-- Комплект 1 -->
          <div class="partner-logo-box" title="Mandra Moments">
            <img src="assets/partners/logo_mandra.png" alt="Mandra Moments" class="partner-img logo-mandra">
          </div>
          <div class="partner-logo-box" title="YOD Group">
            <img src="assets/partners/logo_yod.png" alt="YOD Group" class="partner-img logo-yod">
          </div>
          <div class="partner-logo-box" title="Ekopark Kovalivka">
            <img src="assets/partners/logo_ekopark.png" alt="Ekopark Kovalivka" class="partner-img logo-ekopark">
          </div>
          <div class="partner-logo-box" title="Ribas Hotels Group">
            <img src="assets/partners/logo_ribas.svg" alt="Ribas Hotels Group" class="partner-img logo-ribas">
          </div>
          <div class="partner-logo-box" title="Happy Time">
            <img src="assets/partners/logo_happy_time.png" alt="Happy Time" class="partner-img logo-happytime">
          </div>
          <div class="partner-logo-box" title="TEMO Hotel Design">
            <img src="assets/partners/logo_temo.svg" alt="TEMO Hotel Design" class="partner-img logo-temo">
          </div>

          <!-- Комплект 2 (безперервний безшовний цикл) -->
          <div class="partner-logo-box" title="Mandra Moments" aria-hidden="true">
            <img src="assets/partners/logo_mandra.png" alt="" class="partner-img logo-mandra">
          </div>
          <div class="partner-logo-box" title="YOD Group" aria-hidden="true">
            <img src="assets/partners/logo_yod.png" alt="" class="partner-img logo-yod">
          </div>
          <div class="partner-logo-box" title="Ekopark Kovalivka" aria-hidden="true">
            <img src="assets/partners/logo_ekopark.png" alt="" class="partner-img logo-ekopark">
          </div>
          <div class="partner-logo-box" title="Ribas Hotels Group" aria-hidden="true">
            <img src="assets/partners/logo_ribas.svg" alt="" class="partner-img logo-ribas">
          </div>
          <div class="partner-logo-box" title="Happy Time" aria-hidden="true">
            <img src="assets/partners/logo_happy_time.png" alt="" class="partner-img logo-happytime">
          </div>
          <div class="partner-logo-box" title="TEMO Hotel Design" aria-hidden="true">
            <img src="assets/partners/logo_temo.svg" alt="" class="partner-img logo-temo">
          </div>

          <!-- Комплект 3 (запас для надшироких екранів 2K/4K) -->
          <div class="partner-logo-box" title="Mandra Moments" aria-hidden="true">
            <img src="assets/partners/logo_mandra.png" alt="" class="partner-img logo-mandra">
          </div>
          <div class="partner-logo-box" title="YOD Group" aria-hidden="true">
            <img src="assets/partners/logo_yod.png" alt="" class="partner-img logo-yod">
          </div>
          <div class="partner-logo-box" title="Ekopark Kovalivka" aria-hidden="true">
            <img src="assets/partners/logo_ekopark.png" alt="" class="partner-img logo-ekopark">
          </div>
          <div class="partner-logo-box" title="Ribas Hotels Group" aria-hidden="true">
            <img src="assets/partners/logo_ribas.svg" alt="" class="partner-img logo-ribas">
          </div>
          <div class="partner-logo-box" title="Happy Time" aria-hidden="true">
            <img src="assets/partners/logo_happy_time.png" alt="" class="partner-img logo-happytime">
          </div>
          <div class="partner-logo-box" title="TEMO Hotel Design" aria-hidden="true">
            <img src="assets/partners/logo_temo.svg" alt="" class="partner-img logo-temo">
          </div>
        </div>
      </div>
    </div>
  </section>
'''

petrichor_close = '</section>\n\n  <!-- Sleek Side Tab Trigger -->'
if petrichor_close in content:
    content = content.replace(petrichor_close, '</section>\n' + partners_html + '\n  <!-- Sleek Side Tab Trigger -->', 1)
else:
    print('Warning: petrichor_close pattern not found!')

# 3. Add to translations
ua_old = "mpDivideBtnText: 'Розділити на 3 комплекси'\n      },"
ua_new = "mpDivideBtnText: 'Розділити на 3 комплекси',\n        /* ЕКРАН 6 — ПАРТНЕРИ */\n        partnersTitle: 'Партнери Мандра Інвест'\n      },"
content = content.replace(ua_old, ua_new, 1)

en_old = "mpDivideBtnText: 'Divide into 3 Complexes'\n      }\n    };"
en_new = "mpDivideBtnText: 'Divide into 3 Complexes',\n        /* SCREEN 6 — PARTNERS */\n        partnersTitle: 'Mandra Invest Partners'\n      }\n    };"
content = content.replace(en_old, en_new, 1)

# 4. Add to s2 array
s2_old = "'mpTabAll','mpTab1','mpTab2','mpTab3','mpDivideBtnText'];"
s2_new = "'mpTabAll','mpTab1','mpTab2','mpTab3','mpDivideBtnText',\n                  'partnersTitle'];"
content = content.replace(s2_old, s2_new, 1)

with open('c:/nextweb/mandra/site/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('c:/nextweb/mandra/site/numo-style.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html and numo-style.html successfully!')
