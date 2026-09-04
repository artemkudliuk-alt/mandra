import cv2, numpy as np
from PIL import Image

img = Image.open('c:/nextweb/mandra/site/assets/founders/pine_card_bg.jpg')
arr = np.array(img).astype(np.float32)

# Create a smooth horizontal blend: from x=0 to x=400, replace with dark forest gradient
# Mean color of the blurry background around (100, 100) is roughly (16, 26, 20)
h, w, _ = arr.shape
gradient = np.zeros((h, w, 3), dtype=np.float32)

for y in range(h):
    for x in range(w):
        # subtle vertical gradient in dark green
        t = y / h
        r = 12 + 8 * (1 - t)
        g = 18 + 12 * (1 - t)
        b = 15 + 8 * (1 - t)
        gradient[y, x] = [r, g, b]

# Blend mask: 1.0 on left (x=0..320), fading to 0.0 at x=480..w
blend_mask = np.zeros((h, w, 1), dtype=np.float32)
for x in range(w):
    if x < 300:
        val = 1.0
    elif x < 500:
        val = 1.0 - (x - 300) / 200.0
    else:
        val = 0.0
    blend_mask[:, x, 0] = val

final = arr * (1.0 - blend_mask) + gradient * blend_mask
final = np.clip(final, 0, 255).astype(np.uint8)
res = Image.fromarray(final)
res.save('c:/nextweb/mandra/site/assets/founders/pine_card_clean.jpg', quality=95)
print('Blended dark forest gradient seamlessly!')
