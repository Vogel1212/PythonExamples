n = 1
pair = odd = 0
while n != 0:
    n = int(input('Enter a value: '))
    if n != 0:
        if n % 2 == 0:
            pair += 1
        else:
            odd += 1
print('You typed {} numbers pairs and {} numbers odd'.format(pair,odd))