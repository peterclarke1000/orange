#! /usr/bin/env python3
import json

json_string = '''
{
    "student":[
        {
            "id": 1,
            "name": "Joe",
            "age": 21,
            "full-true": true
        },
        {
             "id": 2,
            "name": "jim",
            "age": 19,
            "full-true": false
        }
    ]
}
'''

data = json.loads(json_string)
data['test'] = True

new_json = json.dumps(data, indent=2)
print(new_json)
new_json = json.dumps(data)
print(new_json)

# print(data['student'][1])
