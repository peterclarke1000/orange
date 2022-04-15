import json

jsonString = '''{"student": [{"id": 1, "name": "Joe", "age": 21, "full-true": true}, {"id": 2, "name": "jim", "age": 19, "full-true": false}], "test": true}'''

data  = json.loads(jsonString)
dataOut = json.dumps(data)
print(dataOut)

dataOut = json.dumps(data, indent=2)
print(dataOut)

