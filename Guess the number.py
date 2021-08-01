# guess the number computer
# import random
# def guess(x):
#     random_number = random.randint(1,x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'guess a number between 1 and {x}:'))
#         if guess < random_number:
#             print("sorry, guess again. too low")
#         elif guess > random_number:
#             print("sorry, guess again. too high")
#     print(f"yay, congrats. you guessed the number {random_number} correctly")
#
# guess(10)

# guess the number(user)
import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (H), too low (L), or correct (C)?.').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'yay the computer guessed your number,{guess}, correctly')


computer_guess(10)