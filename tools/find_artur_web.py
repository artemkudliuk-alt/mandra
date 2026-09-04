import urllib.request, json, re

# Search ribashotelsgroup.ua for team or artur lupashko
url = 'https://ribashotelsgroup.ua/about/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=5) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'https?://[^\s\"\'\<\>]+\.(?:jpg|jpeg|png|webp)', html)
        for m in set(matches):
            if any(k in m.lower() for k in ['lupashko', 'artur', 'team', 'founder', 'author']):
                print('Ribas match:', m)
except Exception as e:
    print('Ribas err:', e)
