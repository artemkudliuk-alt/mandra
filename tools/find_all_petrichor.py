import urllib.request, re

url = 'https://mandra-petrichor.com.ua'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=5) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'https?://[^\s\"\'\<\>]+\.(?:jpg|jpeg|png|webp)', html)
        for m in set(matches):
            print('Img:', m)
except Exception as e:
    print('Err:', e)
