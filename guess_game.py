import random
user_input = input('Enter a single digit number:\t')
guess = random.randrange(0, 9)
if int(user_input) == int(guess):
    print('Congratulations, You have won the lottery!!')
else:
    print('Sorry, please try again!')
