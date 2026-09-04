from PIL import Image, ImageFilter

im = Image.open('C:/Users/Jaku/.gemini/antigravity/brain/07a54e62-2d13-4788-9e45-4800af7daf54/.user_uploaded/media_1788480278916.png').convert('RGB')
c_artur = im.crop((327, 35, 452, 146))
c_artur = c_artur.resize((480, 420), Image.Resampling.LANCZOS)
c_artur = c_artur.filter(ImageFilter.UnsharpMask(radius=1.5, percent=125, threshold=2))
c_artur.save('c:/nextweb/mandra/site/assets/founders/artur_lupashko.jpg', quality=95)
print('Artur cropped exact from reference:', c_artur.size)
