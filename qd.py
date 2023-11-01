#!/usr/bin/python3 
from random import randint
from time import sleep
from datetime import date
import re

#Initiate rolls
roll_one = randint(1,6)
roll_two = randint(1,6)
roll_three = randint(1,6)
roll_four = randint(1,6)
roll_five = randint(1,6)
roll_six = randint(1,6)
days_training = ''
today = date.today()
# get dd.mm.YY
days_training += today.strftime("%d.%m.%Y")

#Ask user which training program doing
while True:
    question = input('0 for Swings + Push-ups or 1 for Snatches [default: Snatches]?')

    #Get default answer if input is empty
    if not question:
        question = 1
        training = 'Snatches'
        print('Snatches it is then!')
        break
    try:
        question = int(question)
        #Exit loop if proper answer
        if question == 0:
            training = 'Swings and Push Ups'
            print('Swings and Push Ups, here we go!')
            break
        elif question == 1:
            question = 1
            training = 'Snatches'
            print('Snatches it is then!')
            break
        else:
            print('I am going to need 0 or 1 from you.')
    except ValueError:
        print("Ah, the audacity! That's not even a number. Please input either 0 or 1.")

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

#Check to see that the number of sets is not the same as last training!
with open('done.txt', 'r') as file:
    lines = file.readlines()
    if not lines:
        match = 0        
    else:
        last_line = lines[-1]

        #Extract the number of sets from last_line using regex
        match = re.search(r'(\d+)\s*sets\.', last_line)
        if match:
            match = int(match.group(1))
        else:
            match = 0

#If rolling the same amount of sets roll again to get Delta variation
while roll_one == match:
    print('Same amount of sets as last time. Rolling again...')
    sleep(1)
    roll_one = randint(1,6)

if roll_one == 1:
    sets = '2 sets' 
    print(sets) 
elif roll_one == 2 or roll_one == 3:
    sets = '3 sets' 
    print(sets)
elif roll_one == 4 or roll_one == 5:
    sets = '4 sets' 
    print(sets)
elif roll_one == 6:
    sets = '5 sets' 
    print(sets)

sleep(1)
print('   Rolling the second die...')
sleep(1)
if roll_two == 1 or 2:
    reps = '5/4 reps/sets' 
    print(reps) 
elif roll_two == 3 or roll_two == 4:
    reps = '5/4 and 10/2 reps/sets' 
    print(reps)
elif roll_two == 5 or roll_two == 6:
    reps = '10/2 reps/sets' 
    print(reps)

# Rolls 3 and 4 are only for Swing and Push Up -training program.
if question == 0:
    sleep(1)
    print('   Rolling the third die...')
    sleep(1)
    if roll_three == 1 or roll_three == 2 or roll_three == 3:
        swing_hands = 'Two-handed Swings'
        print(swing_hands) 
    elif roll_three == 4 or roll_three == 5 or roll_three == 6:
        swing_hands = 'One-handed Swings'
        print(swing_hands) 

    sleep(1)
    print('   Rolling the fourth die...')
    sleep(1)

    if roll_four == 1 or roll_four == 2 or roll_four == 3:
        push_hands = 'Palm Push Ups'
        print(push_hands)
    elif roll_four == 4 or roll_four == 5 or roll_four == 6:
        push_hands = 'Fist Push Ups'
        print(push_hands)

# Roll die for resistance variance if chosen in beginning
if question_resistance == 1:
    sleep(1)
    print('   Rolling the die for variance...')
    sleep(1)
    if roll_five == 1:
        variance = 'Resistance of X-. Down one bell size.'
        print(variance)
    elif roll_five == 2 or roll_five == 3:
        variance = 'X+ resistance. Up one bell size.'
        print(variance)
    else:
        variance = 'Normal resistance.'
        print(variance)
    
sleep(1)

#Make the function to write necessary things to file
def write_to_file(log):
    with open('done.txt', 'a') as file:
        file.write('\n' + log)

#Check if print the things for swings, all or Snatches
if question == 1: #Print Snatch
    if question_resistance == 1: #Print w. resistance
        train = (f'. {training}. {sets}. {reps}. {variance}.')
    else:
        train = (f'. {training}. {sets}. {reps}.')
else: #Print Swings and Push Ups
    if question_resistance == 1: #Print w. resistance
        train = (f'. {training}. {sets}. {reps}. {swing_hands}. {push_hands}. {variance}.')
    else:
        train = (f'. {training}. {sets}. {reps}. {swing_hands}. {push_hands}.')

days_training += train
write_to_file(days_training)

sleep(1)
print('\n   GOOD!')
