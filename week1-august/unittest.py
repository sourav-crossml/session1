import json

json_string = None

with open("data.json") as f:
    json_string = f.read()
try:
    parsed_json = json.loads(json_string)
    formatted_json = json.dumps(parsed_json, indent = 4,sort_keys=True)
    with open("data.json","w") as f:
        f.write(formatted_json)
    print(True)
except Exception as e:
    print(repr(e))