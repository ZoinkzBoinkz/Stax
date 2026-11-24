"""Inline supplements.json into the page template -> index.html (GitHub Pages) and stax-preview.html (artifact)."""
import json, pathlib
here = pathlib.Path(__file__).parent
data = json.loads((here.parent / 'supplements.json').read_text())
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
page = (here / 'template.html').read_text().replace('__DATA__', blob)

# GitHub Pages needs a full document; the artifact host adds its own skeleton.
head_end = page.index('<header class="top">')
full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + page[:head_end] + '</head>\n<body>\n' + page[head_end:] + '\n</body>\n</html>\n')
(here.parent / 'index.html').write_text(full)
(here / 'stax-preview.html').write_text(page)
print(f"index.html {len(full)//1024} KB, preview {len(page)//1024} KB")
