import json
with open('input.json', 'r') as file:
        test_json = file.read().replace('\n', '')
parsed = json.loads(test_json)
with open('result.json', 'w') as outfile:
     json.dump(parsed, outfile, indent=4)