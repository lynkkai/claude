"""Print the poster time: a settled moment near the end of the chosen poster scene."""
import json, sys
v = sys.argv[1]
tl = json.load(open(f'{v}/timeline.json'))
s = tl['scenes'][json.load(open(f'{v}/scenes.json')).get('poster_scene', 0)]
print('%.2f' % (s['end'] - 0.6))
