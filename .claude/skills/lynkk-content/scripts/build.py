"""Turn a scene/image source into the page that gets rendered.

Inlines the Lynkk logo SVG wherever the source says %%LOGO%% and points FONTS/ at the bundled fonts.
Usage: python3 build.py <source.html> <out.html>
"""
import os
import re
import sys

here = os.path.dirname(os.path.abspath(__file__))
assets = os.path.normpath(os.path.join(here, '..', 'assets'))
src_path, out_path = sys.argv[1], sys.argv[2]

svg = open(os.path.join(assets, 'logo.svg')).read()
svg = re.sub(r'\s(width|height|class|style|role|aria-label)="[^"]*"', '', svg)
svg = svg.replace('<svg ', '<svg aria-hidden="true" ', 1)

page = open(src_path).read().replace('%%LOGO%%', svg)
fonts_rel = os.path.relpath(os.path.join(assets, 'fonts'), os.path.dirname(os.path.abspath(out_path)))
page = page.replace('url(FONTS/', f'url({fonts_rel}/')
open(out_path, 'w').write(page)
print('wrote', out_path)
