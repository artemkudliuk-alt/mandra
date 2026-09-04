import cv2, numpy as np
from PIL import Image

# Let's inspect home2.png or home.png
im2 = Image.open('c:/nextweb/mandra/assets/00_maket/home2.png')
print('home2 size:', im2.size)

# Let's see if we can find this founders block in home2.png
# Let's save a low-res preview of home2.png slices:
w, h = im2.size
# Let's slice home2 into 6 vertical chunks to find where the founders block is
for i in range(6):
    y_start = int(i * (h / 6))
    y_end = int((i + 1) * (h / 6))
    slice_img = im2.crop((0, y_start, w, y_end))
    slice_img.thumbnail((400, 400))
    slice_img.save(f'c:/nextweb/mandra/site/assets/home2_slice_{i}.png')
    print(f'Slice {i}: y={y_start}..{y_end}')
