# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Jason Jensen>
# Creation Date: <26 April 2022>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''') # remove the , after hungry
	print()

def chooseCave():
    cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')# remove apostrophes from around 1 or 2. # add new line before 1 and after 2
		cave = input()

	return caves # bring back under "cave = input()" and remove the s from cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3) #change time from 3 seconds to 2 seconds
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2) # change random.randint(1, 2) to random.radint(0, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!'

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y': # add a second = sign before 'yes' and before 'y'
	displayIntro()# add space below
	caveNumber = choosecave() # capitlize cave and add space below
	checkCave(caveNumber)

	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no": #add or "n"
		print("Thanks for planing")
