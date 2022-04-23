import json

file_path = 'chapter10-files-and-exceptions/username.json'
with open(file_path) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")