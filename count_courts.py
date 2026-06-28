import json

with open('egypt_courts_complete.json', encoding='utf-8') as f:
    data = json.load(f)

conf = {}
for r in data:
    c = r.get('confidence', '?')
    conf[c] = conf.get(c, 0) + 1

print(f"Total records: {len(data)}")
for level in ['high', 'medium', 'low', '?']:
    if level in conf:
        print(f"{level.capitalize():>7}: {conf[level]}")
