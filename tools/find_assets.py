import os

keywords = ['lupashko', 'artur', 'boev', 'boiev', 'serhiy', 'founder', 'ribas', 'glamp', 'chalet', 'frame', 'pool']
for root, dirs, files in os.walk('c:/nextweb/mandra/assets'):
    for f in files:
        if any(k in f.lower() for k in keywords):
            print(os.path.join(root, f))
