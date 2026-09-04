from PIL import Image

im2 = Image.open('c:/nextweb/mandra/assets/00_maket/home2.png')
# Crop around y = 3200 to 3900 across full width
crop = im2.crop((0, 3100, im2.width, 3900))
crop.save('c:/nextweb/mandra/site/assets/founders_block_fullres.png')
print('Cropped size:', crop.size)
