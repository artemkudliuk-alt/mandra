import urllib.request, json, re

# Let's search mandra.com.ua or related
for url in ['https://mandra.com.ua', 'https://mandra.com.ua/about', 'https://mandra.ua']:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            matches = re.findall(r'https?://[^\s\"\'\<\>]+\.(?:jpg|jpeg|png|webp)', html)
            for m in set(matches):
                if any(k in m.lower() for k in ['boev', 'boiev', 'serhiy', 'sergey', 'team', 'founder']):
                    print('Match:', m)
    except Exception as e:
        print(url, e)
