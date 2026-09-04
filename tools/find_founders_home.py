import cv2, numpy as np
from PIL import Image

ref_cv = cv2.imread('C:/Users/Jaku/.gemini/antigravity/brain/07a54e62-2d13-4788-9e45-4800af7daf54/.user_uploaded/media_1788480278916.png')
# Take a unique patch from the founders image (Artur Lupashko or the text)
patch = ref_cv[40:90, 330:400] # Artur's face

im_home = cv2.imread('c:/nextweb/mandra/assets/00_maket/home.png')
res = cv2.matchTemplate(cv2.cvtColor(im_home, cv2.COLOR_BGR2GRAY), cv2.cvtColor(patch, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print('Match in home.png:', max_val, max_loc)

if max_val > 0.5:
    x, y = max_loc
    # Crop generous area around it
    crop = im_home[max(0, y-300):y+1200, max(0, x-1000):x+2000]
    cv2.imwrite('c:/nextweb/mandra/site/assets/founders_match_home.png', crop)
    print('Found and saved!')
