import json
import os

for my_file in os.listdir():
    try:
        with open(my_file,'r+') as f:
            value=json.loads(f.read())
            for extract in value:
                print(extract['code'])
    except:
        continue
