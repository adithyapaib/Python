#program to geuss a number  

import random
secret = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

for geuss in range(1,7):
    print('Take a guess.')
    guess = int(input())
    if guess < secret:
        print('Your guess is too low.')
    elif guess > secret:
        print('Your guess is too high.')
    else:
        break
if geuss == secret:
    print('You have run out of guesses. The number was', secret)
else:
    print('Good job! You guessed my number in', geuss, 'guesses!')
