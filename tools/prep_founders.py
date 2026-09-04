import os, cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

out_dir = 'c:/nextweb/mandra/site/assets/founders'
os.makedirs(out_dir, exist_ok=True)

im = Image.open('C:/Users/Jaku/.gemini/antigravity/brain/07a54e62-2d13-4788-9e45-4800af7daf54/.user_uploaded/media_1788480278916.png').convert('RGB')

# 1. Pine background (top left card):
# In the user's screenshot, the text is inside this card.
# If we keep the pine branch background, we can crop just the pine branch or use the card background:
c_pine = im.crop((58, 32, 323, 192))
# upscale 2.5x
c_pine = c_pine.resize((750, 440), Image.Resampling.LANCZOS)
c_pine.save(f'{out_dir}/pine_card_bg.jpg', quality=95)

# 2. Artur Lupashko:
# From original 2048x2048 artur_orig.jpg:
if os.path.exists(f'{out_dir}/artur_orig.jpg'):
    artur_orig = Image.open(f'{out_dir}/artur_orig.jpg').convert('RGB')
    # The reference is a square/portrait bust shot
    # In artur_orig, center is (1024, 1024)
    # Let's crop nicely matching the reference
    w_a, h_a = artur_orig.size
    crop_artur = artur_orig.crop((int(w_a * 0.15), int(h_a * 0.1), int(w_a * 0.85), int(h_a * 0.72)))
    crop_artur = crop_artur.resize((480, 420), Image.Resampling.LANCZOS)
    crop_artur.save(f'{out_dir}/artur_lupashko.jpg', quality=95)
    print('Artur cropped from original HQ photo')
else:
    c_artur = im.crop((326, 34, 452, 146)).resize((480, 420), Image.Resampling.LANCZOS)
    c_artur.save(f'{out_dir}/artur_lupashko.jpg', quality=95)

# 3. Serhiy Boiev:
# Crop cleanly without outer borders
c_serhiy = im.crop((458, 35, 582, 145))
c_serhiy = c_serhiy.resize((480, 420), Image.Resampling.LANCZOS)
# Gentle unsharp mask for crispness
c_serhiy = c_serhiy.filter(ImageFilter.UnsharpMask(radius=1.5, percent=130, threshold=3))
c_serhiy.save(f'{out_dir}/serhiy_boiev.jpg', quality=95)
print('Serhiy cropped and enhanced')

# 4..9 Gallery thumbnails:
# Exact coordinates of 6 thumbnails inside bottom row:
# Bbox in screenshot: y: 198..268
# Total row width: x: 57..582
# Each thumb is approx 82-84 px wide, with 5-6px gap
gallery_boxes = [
    (58, 198, 139, 268),
    (145, 198, 227, 268),
    (233, 198, 314, 268),
    (320, 198, 402, 268),
    (408, 198, 489, 268),
    (495, 198, 577, 268),
]

for idx, box in enumerate(gallery_boxes, 1):
    thumb = im.crop(box)
    # Upscale 3x and sharpen
    thumb_hq = thumb.resize((thumb.width * 4, thumb.height * 4), Image.Resampling.LANCZOS)
    thumb_hq = thumb_hq.filter(ImageFilter.UnsharpMask(radius=1.2, percent=120, threshold=2))
    thumb_hq.save(f'{out_dir}/gallery_{idx}.jpg', quality=95)
    print(f'Gallery {idx} saved: {thumb_hq.size}')
