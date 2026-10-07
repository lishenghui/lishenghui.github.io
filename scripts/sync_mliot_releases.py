"""Generate the MLIoT pip find-links index from public Edgelet releases."""
import html
import json
import os
from pathlib import Path
import urllib.request


def main():
    links = []
    for page in range(1, 101):
        url = f'https://api.github.com/repos/lishenghui/edgelet-releases/releases?per_page=100&page={page}'
        headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'mliot-package-index'}
        if os.environ.get('GH_TOKEN'):
            headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
            releases = json.load(response)
        for release in releases:
            if release.get('draft'):
                continue
            links.extend((asset['name'], asset['browser_download_url']) for asset in release['assets']
                         if asset['name'].startswith('edgelet-') and asset['name'].endswith('.whl'))
        if len(releases) < 100:
            break
    if not links:
        raise RuntimeError('No Edgelet wheels found; refusing to replace the index')
    body = '\n'.join(f'<a href="{html.escape(url, quote=True)}">{html.escape(name)}</a><br>'
                     for name, url in sorted(set(links)))
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Edgelet packages — MLIoT</title></head>
<body><h1>Edgelet packages</h1><p><a href="../">MLIoT teaching resources</a></p>
<pre>python -m pip install -U "edgelet[lab2]" -f https://lishenghui.github.io/teaching/mliot/edgelet-releases/</pre>
{body}
</body></html>
'''
    target = Path(__file__).resolve().parents[1] / 'teaching/mliot/edgelet-releases/index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page)
    print(f'Indexed {len(set(links))} wheels')


if __name__ == '__main__':
    main()
