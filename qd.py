#!/usr/bin/python3 
from random import randint
from time import sleep

#Initiate rolls
roll_one = randint(1,6)
roll_two = randint(1,6)
roll_three = randint(1,6)
roll_four = randint(1,6)
roll_five = randint(1,6)
roll_six = randint(1,6)

#Ask user which training program doing
while True:
    question = input('0 for Swings + Push-ups or 1 for Snatches [default: Snatches]?')

    #Get default answer if input is empty
    if not question:
        question = 1
        print('Snatches it is then!')
        break
    try:
        question = int(question)
        #Exit loop if proper answer
        if question == 0:
            print('Swings and Push Ups, here we go!')
            break
        elif question == 1:
            print('Snatches it is then!')
            break
        else:
            print('I am going to need 0 or 1 from you.')
    except ValueError:
        print("Nope! That's not even a number. Please input either 0 or 1.")

while True:
    question_resistance = input('Do you want varied resistance? 0 for NO, 1 for YES (default NO)')

    #Get default answer if input is empty
    if not question_resistance:
        question_resistance = 0
        print('No Variance')
        break
    try:
        question_resistance = int(question_resistance)
        #Exit loop if proper answer
        if question_resistance == 0:
            print('No Variance')
            break
        elif question_resistance == 1:
            print('Possible variability')
            break
        else:
            print('I am going to need 0 or 1 from you.')
    except ValueError:
        print("Cmon! Input either 0 or 1.")

# Add sleeping to simulate throwing the die
sleep(1)
print('   Rolling...')
sleep(1)
if roll_one == 1:
    print('2 sets') 
elif roll_one == 2 or roll_one == 3:
    print('3 sets')
elif roll_one == 4 or roll_one == 5:
    print('4 sets')
elif roll_one == 6:
    print('5 sets')

sleep(1)
print('   Rolling the second die...')
sleep(1)
if roll_two == 1 or 2:
    print('Sets of 5/4') 
elif roll_two == 3 or roll_two == 4:
    print('Sets of 5/4 and 10/2')
elif roll_two == 5 or roll_two == 6:
    print('Sets of 10/2')

# Rolls 3 and 4 are only for Swing and Push Up -training program.
if question == 0:
    sleep(1)
    print('   Rolling the third die...')
    sleep(1)
    if roll_three == 1 or roll_three == 2 or roll_three == 3:
        print('Two-handed Swings') 
    elif roll_three == 4 or roll_three == 5 or roll_three == 6:
        print('One-handed Swings')

    sleep(1)
    print('   Rolling the fourth die...')
    sleep(1)

    if roll_four == 1 or roll_four == 2 or roll_four == 3:
        print('Palm Push Ups') 
    elif roll_four == 4 or roll_four == 5 or roll_four == 6:
        print('Fist Push Ups')

# Roll die for resistance variance if chosen in beginning

if question_resistance == 1:
    sleep(1)
    print('   Rolling the die for variance...')
    sleep(1)
    if roll_five == 1:
        print('Resistance of X-. Go down one bell size')
    elif roll_five == 2 or roll_five == 3:
        print('X+ resistance. Go up one bell size')
    else:
        print('Normal resistance X. Go Powerful!')
    
sleep(1)
print('   GOOD!')


