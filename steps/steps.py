import os
import time
import shelve
from sys import exit
from steps import journey, calculate
from steps.intro import *
from steps.constants import *
from console import prompt, put, align


def main():

	# Introduction
	printIntro()
	put.divider(APP_LENGTH, character='=')
	print()

	# Change working directory to script's location
	scriptPath = os.path.realpath(__file__)
	scriptDir = os.path.dirname(scriptPath)
	os.chdir(scriptDir)

	# Read data
	with shelve.open(DATA_FILE) as shelf:
		if 'journeys' in shelf.keys():
			journeys = shelf['journeys']
		else:
			journeys = []

	# Hit enter to continue
	input(align.center('[Hit enter to continue]', APP_LENGTH))

	while True:

		put.divider(APP_LENGTH, character='=')
		print()

		# Check data
		if journeys != []:
			hasData = True
		else:
			hasData = False

		# Journeys
		put.headerCenter('Journeys', APP_LENGTH)
		if hasData:
			# List journeys
			print(journey.list(journeys))
		else:
			print(align.center('No journey found!', APP_LENGTH))
		print()

		# Choices
		options = ['Add']
		if hasData:
			options.extend(['Info', 'Edit', 'Delete', 'Clear'])
		options.append('Exit')
		choice = prompt.choiceRows(options, 3)
		put.divider(APP_LENGTH, character='=')
		print()

		# Operations
		if choice == 0:
			# Add a journey
			put.headerCenter('Add a journey', APP_LENGTH)
			if len(journeys) != 26:
				name = input('Enter journey name: ')
				if name.split() != []:
					# Validate goal steps
					while True:
						goal = input('Enter goal steps: ')
						try:
							goal = int(goal)
							if goal <= 0:
								raise ValueError
							break
						except ValueError:
							print('Invalid response.')
					journeys = journey.add(journeys, name, goal)
			else:
				print('Too many journeys!')
			continue
		if hasData:
			if choice == 1:
				# Display information of journey
				print('Display info...')
			elif choice == 2:
				# Edit a journey
				print('Edit journey...')
			elif choice == 3:
				# Delete a journey
				print('Delete journey...')
			elif choice == 4:
				# Clear all journeys
				put.headerCenter('Clear all journeys', APP_LENGTH, newLineBelow=False)
				response = prompt.yesOrNo(prompt='\nAre you sure? (Y/N) ')
				if response == 'Y': 
					journeys = journey.clear()
			else:
				# Exit application
				break
		else:
			# Exit application
			break

	# Write data
	with shelve.open(DATA_FILE) as shelf:
		shelf['journeys'] = journeys

	exit(0)


if __name__ == '__main__':
	main()

