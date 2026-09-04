import os
import cv2, numpy as np
from PIL import Image

# Template match with the user uploaded image
im_ref = Image.open('C:/Users/Jaku/.gemini/antigravity/brain/07a54e62-2d13-4788-9e45-4800af7daf54/.user_uploaded/media_1788480278916.png')
print('Ref size:', im_ref.size)

# Search in home2.png
im2 = Image.open('c:/nextweb/mandra/assets/00_maket/home2.png')

# Let's also check home.png (7305, 7173)
# Let's search home2 first
im2_cv = cv2.imread('c:/nextweb/mandra/assets/00_maket/home2.png')
ref_cv = cv2.imread('C:/Users/Jaku/.gemini/antigravity/brain/07a54e62-2d13-4788-9e45-4800af7daf54/.user_uploaded/media_1788480278916.png')

# Artur Lupashko face crop from ref
artur_face = ref_cv[30:100, 350:420]
res = cv2.matchTemplate(cv2.cvtColor(im2_cv, cv2.COLOR_BGR2GRAY), cv2.cvtColor(artur_face, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print('Match in home2.png:', max_val, max_loc)

if max_val < 0.6:
    # Try home.png
    print('Searching home.png...')
    im1_cv = cv2.imread('c:/nextweb/mandra/assets/00_maket/home.png')
    res1 = cv2.matchTemplate(cv2.cvtColor(im1_cv, cv2.COLOR_BGR2GRAY), cv2.cvtColor(artur_face, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)
    print('Match in home.png:', max_val1, max_loc1)
