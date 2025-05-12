import random
counter = {}
max_count = 0

number = int(input('Enter the number of dice rolls (between 100 and 1,000,000): '))

if number > 1000000 or number < 100:
    print('Please enter a number within the specified range.')

else:
    for _ in range(number):
        dice = random.randint(1, 6)
        if dice not in counter:
            counter[dice] = 1
        else:
            counter[dice] += 1

    for key, value in counter.items():
        if max_count < value:
            max_count = value
            
    for i in range(1, 7):
        for key, value in counter.items():
            if key == i:
                stars_count = (value/max_count) * 10
                countingstars = "*" * int(stars_count)
                percent = value / number * 100
                print(f'{key}: {countingstars} ({value} times, {percent:.2f}%)')    
