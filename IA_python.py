import json

pakistan_fix = []
with open('Pakistan.json', 'r') as file:
    data = json.load(file)
    for line in data:
        if line['high'] != line['low']:
            pakistan_fix.append(line)

print(pakistan_fix)