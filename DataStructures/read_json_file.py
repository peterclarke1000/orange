#! /usr/bin/env python3
import json

with open('students.json','r') as f:
    data = json.load(f)

print(data.items())

with open('data2.json', 'w') as f:
    json.dump(data,f)