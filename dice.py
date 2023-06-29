#Import randint from random
from random import randint

#Declare a variable to roll again
roll_again = ''

#Continue until the user enters either E or e
while(roll_again.lower() != 'e'):
    #Display a prompt
    roll_again = input('Ready to roll? ENTER = Roll, E = EXIT: ')

    #Roll a number from 1 to 6
    num_rolled = randint(1, 6)

    #Print out the rolled number
    print('You rolled a', num_rolled)
