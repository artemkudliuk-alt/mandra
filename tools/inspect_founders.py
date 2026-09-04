import cv2, numpy as np
from PIL import Image

im = Image.open('C:/Users/Jaku/.gemini/antigravity/brain/07a54e62-2d13-4788-9e45-4800af7daf54/.user_uploaded/media_1788480278916.png')
w, h = im.size
print('w, h:', w, h)

# Let's inspect the dark container bounds
arr = np.array(im)
gray = cv2.cvtColor(arr[:,:,:3], cv2.COLOR_RGB2GRAY)
# Background is white (255)
# Container is dark (< 100)
mask = gray < 200
coords = np.argwhere(mask)
y0, x0 = coords.min(axis=0)
y1, x1 = coords.max(axis=0) + 1
print('Dark container bbox:', x0, y0, x1, y1, 'dimensions:', x1-x0, y1-y0)

# Let's crop the container
container = im.crop((x0, y0, x1, y1))
container.save('c:/nextweb/mandra/site/assets/founders_container_raw.png')
