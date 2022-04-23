from random import choice

values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd']

ticket = []
for i in range(0, 4):
    ticket.append(choice(values))

print(f'Lottery: {ticket}')

count = 0
my_ticket = []
while my_ticket != ticket:
    count += 1
    my_ticket = []
    for i in range(0, 4):
        my_ticket.append(choice(values))

print(count)

# the loop ran for 111180 times (for the first test)