"""Inline the Lynkk logo into scene.src.html and write scene.html (the page render.mjs films)."""
import re

svg = open('logo.svg').read()
svg = re.sub(r'\s(width|height|class|style|role|aria-label)="[^"]*"', '', svg)
svg = svg.replace('<svg ', '<svg aria-hidden="true" ', 1)
src = open('scene.src.html').read()
open('scene.html', 'w').write(src.replace('%%LOGO%%', svg))
print('wrote scene.html')
