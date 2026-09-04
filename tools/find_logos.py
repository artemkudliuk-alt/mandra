import urllib.request, re

req = urllib.request.Request('https://temo.com.ua', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'https://temo\.com\.ua/wp-content/uploads/[^\s\"\'\<\>]+', html)
        for m in set(matches):
            if 'logo' in m.lower():
                print('TEMO Logo:', m)
except Exception as e:
    print('Error:', e)
