#write functions here, don't add input('') statements here!

import random

def get_random_number():

    keep_going = 'y'
    number = random.randint(1,5)

    while keep_going == 'y' or keep_going == 'Y':
        guess_number = int(input('Guess a number between 1 and 5: '))

        if guess_number == number:
            keep_going = input('Congratulations, Try again? y or Y: ')
        
        else:
            keep_going = input('Incorrect, Try again? y or Y: ')
            break

    #return number
