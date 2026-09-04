import cv2, numpy as np
from PIL import Image

for name, box in [('logo_ekopark.png', (435, 14, 525, 89)), ('logo_happy_time.png', (358, 88, 432, 152))]:
    im_source = Image.open('C:/Users/Jaku/.gemini/antigravity/brain/07a54e62-2d13-4788-9e45-4800af7daf54/.user_uploaded/media_1788479237486.png')
    c = im_source.crop(box).convert('L')
    
    # 8x upscale
    up = c.resize((c.width * 8, c.height * 8), Image.Resampling.LANCZOS)
    arr = np.array(up)
    
    # Smooth thresholding
    # Gaussian blur slightly to remove pixelation staircases
    blurred = cv2.GaussianBlur(arr, (5, 5), 1.0)
    
    # Sigmoid contrast curve
    # 0 for white background, 255 for black shapes
    alpha = np.clip((230.0 - blurred) * (255.0 / 120.0), 0, 255).astype(np.uint8)
    
    # Clean bounding box
    coords = np.argwhere(alpha > 30)
    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0) + 1
    
    alpha = alpha[y0:y1, x0:x1]
    out_rgba = np.zeros((alpha.shape[0], alpha.shape[1], 4), dtype=np.uint8)
    # RGB is pure black #000000
    out_rgba[:, :, 3] = alpha
    
    res = Image.fromarray(out_rgba, 'RGBA')
    # Resize to standard height 120px
    target_h = 120
    final_w = int(res.width * (target_h / res.height))
    res = res.resize((final_w, target_h), Image.Resampling.LANCZOS)
    res.save(f'c:/nextweb/mandra/site/assets/partners/{name}')
    print(f'Enhanced {name} -> {res.size}')
