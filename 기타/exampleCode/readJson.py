import json

with open('test.json', 'r', encoding='utf-8') as f :
    json_data = json.load(f)
print(json.dumps(json_data, ensure_ascii=False))