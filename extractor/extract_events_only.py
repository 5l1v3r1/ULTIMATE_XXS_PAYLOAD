import json
import os

with open('events.json','r+') as f:
    value=json.loads(f.read())
    for extract in value:
        for i in value[extract]:
            if( i == 'tags'):
                for i in value[extract][i]:
                    print(i['code'])
