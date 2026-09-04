import os
from PIL import Image

out_dir = 'c:/nextweb/mandra/site/assets/founders'
os.makedirs(out_dir, exist_ok=True)

im = Image.open('C:/Users/Jaku/.gemini/antigravity/brain/07a54e62-2d13-4788-9e45-4800af7daf54/.user_uploaded/media_1788480278916.png').convert('RGB')

crops = {
    'pine_bg': (60, 34, 321, 190),
    'artur_lupashko': (326, 34, 452, 146),
    'serhiy_boiev': (457, 34, 583, 146),
    'gallery_1': (58, 198, 140, 269),
    'gallery_2': (146, 198, 227, 269),
    'gallery_3': (233, 198, 314, 269),
    'gallery_4': (320, 198, 402, 269),
    'gallery_5': (407, 198, 489, 269),
    'gallery_6': (495, 198, 577, 269),
}

for name, box in crops.items():
    c = im.crop(box)
    c_high = c.resize((c.width * 3, c.height * 3), Image.Resampling.LANCZOS)
    c_high.save(os.path.join(out_dir, f'{name}.jpg'), quality=95)
    print(f'Saved {name}: {c.size} -> {c_high.size}')
