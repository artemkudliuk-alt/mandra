import cv2, numpy as np
from PIL import Image

img = cv2.imread('c:/nextweb/mandra/site/assets/founders/pine_card_bg.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# The text is white letters on dark background in lower-left: y > 220, x < 650
mask = np.zeros_like(gray)
# threshold for white text
_, text_mask = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
# only apply in bottom-left
text_mask[:int(img.shape[0]*0.45), :] = 0
text_mask[:, int(img.shape[1]*0.8):] = 0

# Dilate slightly to cover text edges
kernel = np.ones((5,5), np.uint8)
text_mask = cv2.dilate(text_mask, kernel, iterations=2)

inpainted = cv2.inpaint(img, text_mask, inpaintRadius=7, flags=cv2.INPAINT_TELEA)
cv2.imwrite('c:/nextweb/mandra/site/assets/founders/pine_card_clean.jpg', inpainted)
print('Inpainted pine card background!')
