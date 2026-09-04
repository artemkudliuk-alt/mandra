import urllib.request, re

for site in ['https://ekoparkkovalivka.com', 'https://ekopark-kovalivka.com', 'https://ekopark-kovalivka.com.ua', 'https://kovalivka-park.com']:
    try:
        req = urllib.request.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            matches = re.findall(r'https?://[^\s\"\'\<\>]+\.(?:svg|png|webp)', html)
            for m in set(matches):
                if 'logo' in m.lower():
                    print('Ekopark logo:', m)
    except Exception as e:
        print(site, e)
