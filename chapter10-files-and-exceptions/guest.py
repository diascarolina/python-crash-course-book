name = input('What is your name? ')

with open('chapter10-files-and-exceptions/guest.txt', 'a') as f:
    f.write(f'{name}\n')