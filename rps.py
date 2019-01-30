#'Rock','Paper','Scissors' game

import random

still_playing = True
wins = 0
losses = 0
ties = 0

def end_of_hand():
	print('You have ' + str(wins) + ' wins, ' + str(losses) + ' losses, and ' + str(ties) + ' ties.')
	control_loop = True
	while control_loop==True:
		cont = str(input('Would you like to continue playing? You can enter y/n for yes/no:\n'))
		if(cont.lower()=='y' or cont.lower()=='yes'):
			control_loop = False
		elif(cont.lower()=='n' or cont.lower()=='no'):
			global still_playing
			still_playing = False
			control_loop = False
			print('Thanks for playing!')
		else:
			print('\nPlease enter a valid yes/no. You can use y/n.')

# Maiu
print('Welcome to rock paper scissors!')
while still_playing == True: 
	try:
		user_choice = int(input('Please select a choice by typing 1 for rock, 2 for paper, and 3 for scissors:\n'))
		comp_choice = random.randint(1, 3)
		if(user_choice==1):
			print('You have selected rock.')
		elif(user_choice==2):
			print('You have selected paper.')		
		elif(user_choice==3):
			print('You have selected scissors.')
		if(comp_choice==1):
			print('The computer has selected rock.')
		elif(comp_choice==2):
			print('The computer has selected paper.')		
		elif(comp_choice==3):
			print('The computer has selected scissors.')
		if((user_choice==1 and comp_choice==1) or (user_choice==2 and comp_choice==2) or (user_choice==3 and comp_choice==3)):
			ties += 1
			print('You have tied the computer.')
			end_of_hand()
		elif((user_choice==1 and comp_choice==3) or (user_choice==2 and comp_choice==1) or (user_choice==3 and comp_choice==2)):
			wins += 1
			print('You beat the computer.')
			end_of_hand()
		elif((user_choice==1 and comp_choice==2) or (user_choice==2 and comp_choice==3) or (user_choice==3 and comp_choice==1)):
			losses += 1
			print('You have lost to the computer.')
			end_of_hand()
	except ValueError:
		print('Error, incorrect input.') 
