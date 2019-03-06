import random

range_limit = 11 
random = random.randint(1,range_limit)
user_input = int(input(f"Please choose a number between 1 and {range_limit - 1} > "))

while user_input != random:
    print('Please try again')
    if user_input < random:
        print(f'Please choose a number that is higher than {user_input}')
    else:
        print(f'Please choose a number that is lover than {user_input}')
    user_input = int(input(f"Please choose a number between 1 and {range_limit - 1} > "))

if user_input == random:
    print("You guessed it!")
