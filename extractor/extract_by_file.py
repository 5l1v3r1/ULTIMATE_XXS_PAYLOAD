#special_tags.json
#encodings.json
#classic.json
import json
import os

with open('classic.json','r+') as f:
    value=json.loads(f.read())
    for extract in value:
        print(extract['code'])
