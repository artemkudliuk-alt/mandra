---
name: mandra-design-system
description: >
  Official Design System & DNA Lock for the Mandra Invest luxury resort platform.
  Enforces exact brand colors, 30 Ukrainian Cyrillic architectural typography standards
  with large monumental font sizing, borderless Liquid Glass materials, bespoke SVG iconography,
  free-floating button geometries, and bilingual Ukrainian/English architecture across all screens.
---

# Mandra Invest — Official Design System & DNA Lock

This skill codifies the immutable design tokens, layout rules, typography scale, color palette, and component patterns established and approved for **MANDRA Invest** (Karpaty Luxury Chalet Investment).

---

## 1. Immutable Brand DNA & Visual Hierarchy

### Rule 1: Authentic Architecture Lock (Zero Hallucination)
- **Reference**: The authentic photo asset is `site/assets/bg_hero.jpg` (4K genuine Mandra A-frame chalet with wooden outdoor tub and terrace in the Carpathian forest at sunset).
- Never hallucinate, alter, or replace the chalets with generic AI cottages. All architectural representations must follow the real Mandra chalet DNA.

### Rule 2: Monumental Font Sizing (CRITICAL)
> *"Помни, что у нас текста не маленькие а большие размеры шрифтов."*
- **Main Hero Headline**: `3.8vw` – `5.2vw` (min 48px, max 84px on desktop), bold (700–800), tight line-height (`1.12`–`1.18`), negative tracking (`-0.02em`).
- **Hero Subtitle / Description**: `1.15vw` – `1.45vw` (min 16px, max 22px on desktop), `Manrope` (400–500), line-height `1.6`, opacity `0.85`.
- **Section Headers on Subsequent Screens**: `3.0vw` – `4.5vw` (never small generic 24px headings!).
- **Card Titles & Stat Callouts**: `2.2vw` – `3.6vw` bold.
- **Body Text**: `1.0vw` – `1.2vw` (15px–18px), generous line-height `1.6`–`1.7`.

### Rule 3: Exact Two-Block Text Structure for Hero
The Hero screen consists strictly of two text blocks:
1. **Block 1 (Main Headline)**:  
   *UA*: `MANDRA Invest — дохідна нерухомість, у яку хочеться повертатися`  
   *EN*: `MANDRA Invest — high-yield real estate you want to return to`
2. **Block 2 (Subtitle / Description)**:  
   *UA*: `Створюємо відпочинкові проєкти, що поєднують нерухомість, сервіс і інвестиційну цінність у Карпатах.`  
   *EN*: `Creating resort projects combining real estate, premium service and investment value in the Carpathians.`

---

## 2. Color Palette & Lighting Tokens

| Token | Hex / Value | Usage |
|---|---|---|
| `--accent-color` | `#81B873` | Main CTA buttons (all styles), active states, underlines, badge icons. Warm Carpathian sage green. |
| `--accent-hover` | `#96C989` | Hover state for accent buttons. |
| `--btn-text-color` | `#0E1F0B` | Deep pine black text on `#81B873` buttons for maximum contrast. |
| `--top-btn-bg` | `#DEF7D7` | Pale pastel mint cream for top header button (`Онлайн заявка`) and phone badge. |
| `--top-btn-text` | `#12240E` | Deep pine green text on `#DEF7D7`. |
| `--top-btn-hover` | `#EBFCE6` | Hover state for top mint button. |
| `--bg-dark` | `#121212` | Foundation background behind photography. Pure neutral graphite gray (STRICTLY NO BLUE HUE). |
| `--bg-scrim-top` | `rgba(18, 18, 18, 0.56)` | Neutral dark gray atmospheric lighting (top). |
| `--bg-scrim-left`| `rgba(18, 18, 18, 0.64)` | Neutral dark gray atmospheric lighting (left). |
| `--footer-bg` | `#141414` | Neutral architectural graphite gray for footer. Zero blue hue. |

### Zero Blue Hue & Scrim Pollution Rule
- **Strictly No Blue Tint**: Mandra has no blue color tokens. All dark backgrounds and surfaces must use pure neutral dark gray (`#121212`, `#141414`, `#161616`) or deep pine black, never navy or midnight blue (`#07090D`).
- **No colored glowing radial shadows** or dirty green blurred spots under buttons (`box-shadow: none !important; filter: none !important;`). The natural terrace wood and grass remain clean.

---

## 3. Borderless Liquid Glass Standards

### Full-Width Header Bar (`.top-navbar`)
- **Span**: 100% width across the entire screen edge-to-edge.
- **Material**: `background: rgba(7, 10, 15, 0.22);` with `backdrop-filter: blur(20px);`.
- **Border**: Strictly `border: none;` (no bottom lines, no dark borders).
- **Padding**: `1.1vw 3.6vw`.

### Action Capsules (`.lang-capsule`, `.phone-capsule`)
- **Material**: `background: rgba(255, 255, 255, 0.08);` with `backdrop-filter: blur(16px);`.
- **Borders**: Strictly `border: none; box-shadow: none;`.
- **Shape**: Rounded pill (`border-radius: 999px;`).

---

## 4. Typography System (30 Curated Ukrainian Fonts)

All fonts must have 100% Cyrillic Ukrainian support (`І`, `Ї`, `Є`):

1. **Unbounded** — Modern wide architectural (Default headline)
2. **Manrope** — Swiss-inspired clean grotesque (Default body/subtitle)
3. **Forum** — Roman classical resort antiqua
4. **Prata** — Glossy editorial luxury serif
5. **Tenor Sans** — Scandinavian minimalist elegance
6. **Montserrat** — Confident geometric grotesque
7. **Playfair Display** — High-fashion magazine serif
8. **Oswald** — Condensed monumental poster display
9. **Rubik** — Soft luxury rounded geometric
10. **Cormorant Garamond** — High editorial haute-couture serif
11. **Inter** — Neutral tech precision
12. **Cinzel** — Roman monumental titling
13. **Syne** — Avant-garde NUMO style display
14. **Comfortaa** — Organic welcoming geometry
15. **Raleway** — Refined high-contrast grotesque
16. **Lora** — Literary contemporary serif
17. **Mulish** — Nordic quiet luxury
18. **Exo 2** — Futuristic architectural
19. **Alumni Sans** — Ultra-tall skyscraper grotesque
20. **Jost** — German clean geometric
21. **Commissioner** — Neo-grotesque Swiss precision
22. **El Messiri** — Delicate organic modern
23. **Spectral** — Book and press editorial
24. **Russo One** — Brutalist block monumental
25. **Yeseva One** — Artistic high-contrast serif
26. **Philosopher** — Art Nouveau modern antiqua
27. **Fira Sans** — Industrial sharp clarity
28. **Podkova** — Architectural slab serif
29. **Uni Sans Heavy** — Monumental uppercase titling (local)
30. **Cocogoose** — Italian compressed display (local)

---

## 5. Screen 1 Components & Layout Specifications

### Circular Architectural Button (`.cta-btn-circle`)
- **Dimensions**: `width: 8.8vw; height: 8.8vw; min-width: 120px; min-height: 120px;` (circular).
- **Background**: `#81B873` (sage green).
- **Text**: `ДІЗНАТИСЯ` / `БІЛЬШЕ` (`0.8vw`, bold 800, `letter-spacing: 0.1em`, color `#0E1F0B`).
- **Arrow**: Custom vector SVG arrow (`viewBox="0 0 24 24"`, `line x1="6" y1="18" x2="18" y2="6"`, `polyline points="9 6 18 6 18 15"`, stroke-width `2.6`).
- **Hover**: Scales to `1.06`, arrow glides diagonally `translate(3px, -3px)`.
- **Default Coordinates**: `left: 3.6vw; top: 80vh;`.

### Bottom Center Scroll Indicator (`.scroll-indicator`)
- **Position**: `position: absolute; bottom: 2.6vh; left: 50%; transform: translateX(-50%);`.
- **Text**: `SCROLL` (uppercase, bold 700, `letter-spacing: 0.18em`, font `Manrope`).
- **Indicator**: Vertical 22px line with fluid keyframe pulse downwards (`animation: scrollDrop 2.2s infinite`).

### Bilingual Architecture (`UA` / `EN`)
- All user-facing copy is mapped in a live bilingual dictionary.
- The `[ 🌐 UA | EN ]` capsule toggles the entire page seamlessly between Ukrainian and English without reloading.

---

## 6. Guidelines for Subsequent Screens (Screen 2+)

When designing subsequent screens:
1. **Inherit All Design Tokens**: Use identical `--accent-color` (`#81B873`), `--top-btn-bg` (`#DEF7D7`), font families (`Unbounded` / `Manrope`), and borderless sheer glass surfaces.
2. **Never Shrink Headers**: Maintain large, confident typographic hierarchy (`3.0vw`–`4.5vw`).
3. **Bilingual Completeness**: Every new section must provide both Ukrainian and English copy in the translation engine.
4. **Cinematic Depth**: Use authentic Carpathian photography, subtle glass cards, and generous white space that lets the design breathe.

---

## 7. Screen 2: Manifesto Section (`#about`) — LOCKED & APPROVED

- **Layout & Canvas**: Pure architectural white `#FFFFFF` background, monumental height `min-height: 128vh; padding: 9vw 5vw;`.
- **Typographic Rhythm (Bold Lead + Refined Body)**:
  - **Lead Sentence (Heavy/Authoritative)**: `.manifesto-lead-bold` (`font-weight: 800; color: #0E1F0B;`):  
    *UA*: `Від ідеї — до працюючого готельного продукту [КАПСУЛА 1].`  
    *EN*: `From vision to a thriving hospitality product [CAPSULE 1].`
  - **Body Sentences (Refined/Light)**: `.manifesto-body-light` (`font-weight: 300; color: #2D3740; line-height: 1.82;`):  
    *UA*: `Mandra Invest — відділ продажу дохідних готельних проєктів девелопера...`  
    *EN*: `Mandra Invest is the official investment division of developer Mandra Moments...`
- **Doubled Panoramic Inline Image Capsules (`.inline-capsule`)**:
  - Dimensions: `width: 10.8vw; height: 5.2vw; min-width: 140px; min-height: 68px;`.
  - Geometry: `border-radius: 999px; overflow: hidden; margin: 0 0.8vw; vertical-align: middle; transform: translateY(-0.25vw);`.
  - Elevation: `box-shadow: 0 12px 34px rgba(0, 0, 0, 0.16);`.
  - 4 Capsules: 01. A-frame chalet with tub, 02. Founders & partners, 03. Mountain forest panorama, 04. Luxury chalet interior.

---

## 8. Screen 3: Showcase Section (`#showcase`) — LOCKED & APPROVED

- **Title**: `Ми відповідаємо за` (UA) / `We are responsible for` (EN) (`3.8vw`, bold 800).
- **Subtitle**: `Локація, ринок, концепція, інфраструктура та сервіс — повний цикл реалізації проєкту.`
- **2x2 Grid of 4 Quadrants**:
  - `01. АНАЛІЗ` — «Локація, ринок та майбутня аудиторія.»
  - `02. КОНЦЕПЦІЯ ТА ДЕВЕЛОПМЕНТ` — «Позиціонування, продукт, проєктування, будівництво та реалізація.»
  - `03. ІНФРАСТРУКТУРА ТА УПРАВЛІННЯ` — «Створення просторів і сервісів, підготовка комплексу до запуску та професійне управління»
  - `04. РОБОТА З ІНВЕСТОРАМИ` — «Супровід від вибору об'єкта до отримання доходу.»
