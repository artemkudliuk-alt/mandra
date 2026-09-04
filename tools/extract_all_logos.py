import os, cv2
import numpy as np
from PIL import Image

out_dir = 'c:/nextweb/mandra/site/assets/partners'
os.makedirs(out_dir, exist_ok=True)

# 1. TEMO: Convert downloaded SVG or make clean PNG
# 2. RIBAS: From logo_ribas.svg
# 3. YOD: From logo_yod_black.webp
# 4. MANDRA: From Logo_Mandra (3).png
# 5. EKOPARK: Cut from media_1788479237486.png and upscale/threshold
# 6. HAPPY TIME: Cut from media_1788479237486.png and upscale/threshold

im_source = Image.open('C:/Users/Jaku/.gemini/antigravity/brain/07a54e62-2d13-4788-9e45-4800af7daf54/.user_uploaded/media_1788479237486.png')

# Precise crops from source image
# Let's inspect source dimensions (646 x 164)
# We can crop and process each logo with alpha transparency & pure black pixels:

def extract_clean_logo(box, out_name, target_h=120):
    cropped = im_source.crop(box).convert('L')
    # Resize with LANCZOS to 4x
    large = cropped.resize((cropped.width * 4, cropped.height * 4), Image.Resampling.LANCZOS)
    arr = np.array(large)
    
    # Invert so black logo becomes bright mask
    # background is white (255)
    # Thresholding with soft antialiasing
    # Value < 220 is part of logo
    alpha = np.zeros_like(arr, dtype=np.uint8)
    # Smooth alpha ramp
    mask = arr < 240
    # Map 240->0, 80->255
    alpha = np.clip((240.0 - arr) * (255.0 / 160.0), 0, 255).astype(np.uint8)
    
    # Pure black RGB with calculated alpha
    black_rgb = np.zeros((arr.shape[0], arr.shape[1], 3), dtype=np.uint8)
    rgba = np.dstack((black_rgb, alpha))
    
    # Trim empty borders
    coords = np.argwhere(alpha > 20)
    if len(coords) > 0:
        y0, x0 = coords.min(axis=0)
        y1, x1 = coords.max(axis=0) + 1
        rgba = rgba[y0:y1, x0:x1]
        
    res = Image.fromarray(rgba, 'RGBA')
    # Scale to standard height
    aspect = res.width / res.height
    final_w = int(target_h * aspect)
    res = res.resize((final_w, target_h), Image.Resampling.LANCZOS)
    res.save(os.path.join(out_dir, out_name))
    print(f'Saved {out_name}: {res.size}')

# Mandra Moments: (265, 20, 365, 85)
extract_clean_logo((265, 20, 365, 85), 'logo_mandra_moments.png', target_h=80)

# YOD Group: (360, 15, 435, 85)
extract_clean_logo((360, 15, 435, 85), 'logo_yod.png', target_h=90)

# Ekopark Kovalivka: (435, 15, 525, 88)
extract_clean_logo((435, 15, 525, 88), 'logo_ekopark.png', target_h=90)

# Ribas Hotels Group: (268, 90, 355, 150)
extract_clean_logo((268, 90, 355, 150), 'logo_ribas.png', target_h=75)

# Happy Time: (360, 90, 430, 150)
extract_clean_logo((360, 90, 430, 150), 'logo_happy_time.png', target_h=75)

# TEMO Hotel Design: (430, 90, 525, 150)
extract_clean_logo((430, 90, 525, 150), 'logo_temo.png', target_h=60)

