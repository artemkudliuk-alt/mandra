import urllib.request, re

# Download TEMO logo
req = urllib.request.Request('https://temo.com.ua/wp-content/uploads/2024/06/logo.svg', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    data = resp.read()
    with open('c:/nextweb/mandra/site/assets/logo_temo.svg', 'wb') as f:
        f.write(data)
    print('TEMO SVG downloaded, size:', len(data))

# Check Happy Time
for site in ['https://happytime.od.ua', 'https://happy-time.ua']:
    try:
        req = urllib.request.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            matches = re.findall(r'https?://[^\s\"\'\<\>]+\.(?:svg|png|webp)', html)
            for m in set(matches):
                if 'logo' in m.lower():
                    print('Happy Time logo:', m)
    except Exception as e:
        print(site, e)
