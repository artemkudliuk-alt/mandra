import urllib.request, re

url = 'https://mandra-petrichor.com.ua'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=5) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'https?://[^\s\"\'\<\>]+\.(?:jpg|jpeg|png|webp)', html)
        for m in set(matches):
            if any(k in m.lower() for k in ['boev', 'boiev', 'lupashko', 'founder', 'artur', 'serg']):
                print('Match on petrichor:', m)
except Exception as e:
    print('Petrichor err:', e)
