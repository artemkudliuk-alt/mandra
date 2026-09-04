from PIL import Image

im = Image.open('C:/Users/Jaku/.gemini/antigravity/brain/07a54e62-2d13-4788-9e45-4800af7daf54/.user_uploaded/media_1788480278916.png').convert('RGB')
out_dir = 'c:/nextweb/mandra/site/assets/founders'

# Look at y=230 across x=50..600 to find gaps between cards
import numpy as np
arr = np.array(im)
row = arr[230, 50:600]
# Dark gap between cards has low brightness (< 40)
# Card photos have higher brightness
# Let's find columns where brightness is high
bright = np.mean(row, axis=1)

# Card 5:
c5 = im.crop((418, 201, 486, 267)).resize((360, 310), Image.Resampling.LANCZOS)
c5.save(f'{out_dir}/gallery_5.jpg', quality=95)

# Card 1:
c1 = im.crop((61, 201, 137, 267)).resize((360, 310), Image.Resampling.LANCZOS)
c1.save(f'{out_dir}/gallery_1.jpg', quality=95)

# Card 2:
c2 = im.crop((149, 201, 224, 267)).resize((360, 310), Image.Resampling.LANCZOS)
c2.save(f'{out_dir}/gallery_2.jpg', quality=95)

# Card 3:
c3 = im.crop((237, 201, 311, 267)).resize((360, 310), Image.Resampling.LANCZOS)
c3.save(f'{out_dir}/gallery_3.jpg', quality=95)

# Card 4:
c4 = im.crop((324, 201, 399, 267)).resize((360, 310), Image.Resampling.LANCZOS)
c4.save(f'{out_dir}/gallery_4.jpg', quality=95)

# Card 6:
c6 = im.crop((498, 201, 574, 267)).resize((360, 310), Image.Resampling.LANCZOS)
c6.save(f'{out_dir}/gallery_6.jpg', quality=95)

print('Recropped all 6 gallery cards cleanly!')
