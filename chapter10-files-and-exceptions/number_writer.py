import json

numbers = [2, 3, 5, 7, 11, 13]

file_path = 'chapter10-files-and-exceptions/numbers.json'
with open(file_path, 'w') as f:
    json.dump(numbers, f)