"""Мінімальний клієнт WaveSpeed: залити референси, запустити модель, дочекатись, скачати.

Ключ читається з .env (WAVESPEED_API_KEY) — у код і коміти він не потрапляє.

    python tools/wavespeed.py openai/gpt-image-2.5-sunburst/edit out.png \
        --prompt "..." --image ref1.jpg --image ref2.png \
        --aspect_ratio 16:9 --resolution 2k --quality max
"""
import argparse
import io
import os
import sys
import time

import requests

API = 'https://api.wavespeed.ai/api/v3'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def api_key():
    for line in io.open(os.path.join(ROOT, '.env'), encoding='utf-8'):
        if line.startswith('WAVESPEED_API_KEY='):
            return line.split('=', 1)[1].strip()
    sys.exit('WAVESPEED_API_KEY немає в .env')


def upload(path, headers):
    """Локальний файл → тимчасовий URL WaveSpeed (живе 7 днів)."""
    with open(path, 'rb') as f:
        r = requests.post(API + '/media/upload/binary', headers=headers,
                          files={'file': (os.path.basename(path), f)}, timeout=300)
    r.raise_for_status()
    return r.json()['data']['download_url']


def run(model, payload, headers, timeout=1200):
    r = requests.post('%s/%s' % (API, model), headers=headers, json=payload, timeout=120)
    if not r.ok:
        sys.exit('запит відхилено %s: %s' % (r.status_code, r.text[:500]))
    pid = r.json()['data']['id']
    t0 = time.time()
    while time.time() - t0 < timeout:
        time.sleep(4)
        d = requests.get('%s/predictions/%s/result' % (API, pid), headers=headers, timeout=60).json()['data']
        if d['status'] == 'completed':
            return d['outputs']
        if d['status'] in ('failed', 'cancelled', 'timeout', 'deleted'):
            sys.exit('модель повернула %s: %s' % (d['status'], d.get('error')))
    sys.exit('не дочекались результату за %d с' % timeout)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('model')
    ap.add_argument('out')
    ap.add_argument('--prompt', required=True)
    ap.add_argument('--image', action='append', default=[])
    ap.add_argument('--aspect_ratio')
    ap.add_argument('--resolution')
    ap.add_argument('--quality')
    a = ap.parse_args()

    headers = {'Authorization': 'Bearer ' + api_key()}
    payload = {'prompt': a.prompt}
    if a.image:
        payload['images'] = [upload(p, headers) for p in a.image]
    for k in ('aspect_ratio', 'resolution', 'quality'):
        if getattr(a, k):
            payload[k] = getattr(a, k)

    url = run(a.model, payload, headers)[0]
    img = requests.get(url, timeout=300)
    img.raise_for_status()
    with open(a.out, 'wb') as f:
        f.write(img.content)
    print(a.out)


if __name__ == '__main__':
    main()
