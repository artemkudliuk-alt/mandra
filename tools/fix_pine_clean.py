import cv2, numpy as np
from PIL import Image

# In pine_card_bg.jpg (780 x 460):
# y from 0 to 220 has NO text!
im = Image.open('c:/nextweb/mandra/site/assets/founders/pine_card_bg.jpg')
arr = np.array(im)
h, w, _ = arr.shape

# The clean pine branch is at x > 480, y < 220
# Let's clone/tile the clean dark background and pine branch:
clean_top = arr[0:220, :] # 220 height clean

# For the lower half y > 220:
# Left side (x < 500) is just dark forest: fill with solid / subtle gradient from top
out = arr.copy()
# Fill lower-left with smooth vertical continuation of the dark forest from y=200
for y in range(210, h):
    for x in range(w):
        if x < 480:
            # pick color from clean upper region around (x, 180..200)
            src_y = 180 + (x % 20)
            out[y, x] = arr[src_y, x]
        elif x < 540:
            # smooth horizontal blend between clean dark and branch
            blend = (x - 480) / 60.0
            src_y = 180 + (x % 20)
            out[y, x] = (1.0 - blend) * arr[src_y, x] + blend * arr[y, x]

# Apply slight Gaussian blur to the lower-left to ensure complete silky smoothness
roi = out[210:h, 0:500]
blurred_roi = cv2.GaussianBlur(roi, (21, 21), 0)
out[210:h, 0:500] = blurred_roi

res = Image.fromarray(out)
res.save('c:/nextweb/mandra/site/assets/founders/pine_card_clean.jpg', quality=95)
print('Perfect zero-text pine background created!')
