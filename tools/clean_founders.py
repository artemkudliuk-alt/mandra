from PIL import Image, ImageFilter

im = Image.open('C:/Users/Jaku/.gemini/antigravity/brain/07a54e62-2d13-4788-9e45-4800af7daf54/.user_uploaded/media_1788480278916.png').convert('RGB')

# Artur: x=330..450, y=36..144
c_artur = im.crop((330, 36, 450, 144)).resize((480, 430), Image.Resampling.LANCZOS)
c_artur = c_artur.filter(ImageFilter.UnsharpMask(radius=1.5, percent=130, threshold=2))
c_artur.save('c:/nextweb/mandra/site/assets/founders/artur_lupashko.jpg', quality=95)

# Serhiy: x=460..580, y=36..144
c_serhiy = im.crop((460, 36, 580, 144)).resize((480, 430), Image.Resampling.LANCZOS)
c_serhiy = c_serhiy.filter(ImageFilter.UnsharpMask(radius=1.5, percent=130, threshold=2))
c_serhiy.save('c:/nextweb/mandra/site/assets/founders/serhiy_boiev.jpg', quality=95)

# Pine background (clean inside without text, or we can use the original crop with dark gradient overlay):
c_pine = im.crop((60, 35, 321, 190)).resize((780, 460), Image.Resampling.LANCZOS)
c_pine.save('c:/nextweb/mandra/site/assets/founders/pine_card_bg.jpg', quality=95)

print('Cleaned Artur, Serhiy, and Pine BG!')
