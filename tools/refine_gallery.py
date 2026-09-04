from PIL import Image, ImageFilter

im = Image.open('C:/Users/Jaku/.gemini/antigravity/brain/07a54e62-2d13-4788-9e45-4800af7daf54/.user_uploaded/media_1788480278916.png').convert('RGB')
out_dir = 'c:/nextweb/mandra/site/assets/founders'

# Refined tight boxes inside each card (avoiding outer borders)
gallery_refined = [
    (60, 200, 137, 267),  # 1: interior
    (148, 200, 225, 267), # 2: pool
    (235, 200, 312, 267), # 3: village
    (322, 200, 400, 267), # 4: terrace
    (410, 200, 487, 267), # 5: a-frame
    (497, 200, 575, 267), # 6: tents lawn
]

for idx, box in enumerate(gallery_refined, 1):
    c = im.crop(box)
    c_hq = c.resize((360, 310), Image.Resampling.LANCZOS)
    c_hq = c_hq.filter(ImageFilter.UnsharpMask(radius=1.5, percent=125, threshold=2))
    c_hq.save(f'{out_dir}/gallery_{idx}.jpg', quality=95)
    print(f'Refined gallery {idx}: {box} -> {c_hq.size}')
