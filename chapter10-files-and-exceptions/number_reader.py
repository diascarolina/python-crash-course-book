import json

file_path = 'chapter10-files-and-exceptions/numbers.json'
with open(file_path) as f:
    numbers = json.load(f)

print(numbers)