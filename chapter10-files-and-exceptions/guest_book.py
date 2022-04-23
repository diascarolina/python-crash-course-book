with open('chapter10-files-and-exceptions/guest_book.txt', 'a') as f:
    name = ''
    while name != 'q':
        name = input("What is your name? (Press 'q' to quit) ")
        f.write(f'{name}\n')
        print(f'Hello, {name}!')