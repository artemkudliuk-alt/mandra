from PIL import Image

# 1. YOD
im_yod = Image.open('c:/nextweb/mandra/assets/12_brand/logo_yod_black.webp').convert('RGBA')
# Make white background transparent
arr = list(im_yod.getdata())
new_arr = []
for r, g, b, a in arr:
    if r > 240 and g > 240 and b > 240:
        new_arr.append((0, 0, 0, 0))
    else:
        new_arr.append((0, 0, 0, 255))
im_yod.putdata(new_arr)
im_yod.save('c:/nextweb/mandra/site/assets/partners/logo_yod.png')
print('YOD saved:', im_yod.size)

# 2. RIBAS: render SVG to high-res PNG or use SVG directly!
# 3. TEMO: use SVG directly!
