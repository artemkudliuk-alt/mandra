"""Мінімальний клієнт OpenAI Images: згенерувати кадр за референсами.

Ключ читається з .env (OPENAI_API_KEY) — у код і коміти він не потрапляє.

    python tools/openai_image.py out.png --prompt "..." --image ref1.jpg --image ref2.webp \
        --size 1536x1024 --quality high
"""
import argparse
import base64
import io
import os
import sys

import requests
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def api_key():
    for line in io.open(os.path.join(ROOT, '.env'), encoding='utf-8'):
        if line.startswith('OPENAI_API_KEY='):
            return line.split('=', 1)[1].strip()
    sys.exit('OPENAI_API_KEY немає в .env')


def as_png(path, max_side=1536):
    """Референс → PNG не більший за max_side: великі картинки лише дорожчають."""
    im = Image.open(path).convert('RGB')
    im.thumbnail((max_side, max_side))
    buf = io.BytesIO()
    im.save(buf, 'PNG')
    return (os.path.splitext(os.path.basename(path))[0] + '.png', buf.getvalue(), 'image/png')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out')
    ap.add_argument('--prompt', required=True)
    ap.add_argument('--image', action='append', default=[])
    ap.add_argument('--model', default='gpt-image-2.5-sunburst')
    ap.add_argument('--size', default='1536x1024')
    ap.add_argument('--quality', default='high')
    a = ap.parse_args()

    headers = {'Authorization': 'Bearer ' + api_key()}
    data = {'model': a.model, 'prompt': a.prompt, 'size': a.size, 'quality': a.quality, 'n': '1'}
    if a.image:
        files = [('image[]', as_png(p)) for p in a.image]
        r = requests.post('https://api.openai.com/v1/images/edits', headers=headers,
                          data=data, files=files, timeout=600)
    else:
        r = requests.post('https://api.openai.com/v1/images/generations', headers=headers,
                          json=data, timeout=600)
    if not r.ok:
        sys.exit('запит відхилено %s: %s' % (r.status_code, r.text[:600]))
    j = r.json()
    with open(a.out, 'wb') as f:
        f.write(base64.b64decode(j['data'][0]['b64_json']))
    print('saved', a.out, j.get('usage', ''))


if __name__ == '__main__':
    main()
