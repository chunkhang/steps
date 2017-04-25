import os
import time
import shelve
from sys import exit
from steps.intro import *
from steps.constants import *
from console import prompt, put, align


def main():

	# Introduction
	printIntro()

	# Change working directory to script's location
	scriptPath = os.path.realpath(__file__)
	scriptDir = os.path.dirname(scriptPath)
	os.chdir(scriptDir)

	firstTime = True

	while True:

		put.divider(APP_LENGTH, character='=')
		print()

		with shelve.open(DATA_FILE) as shelf:

			# Get keys from shelf
			if 'journeys' not in shelf.keys():
				shelf['journeys'] = []
			journeys = shelf['journeys']
			if len(journeys) == 0:
				hasData = False
			else:
				hasData = True

			# Hit enter to continue
			if firstTime:
				input(align.center('[Hit enter to continue]', APP_LENGTH))
				put.divider(APP_LENGTH, character='=')
				print()
				firstTime = False

			# Journeys
			put.headerCenter('Journeys', APP_LENGTH)
			if hasData:
				# List journeys
				for i in range(len(journeys)):
					print('(%s) %s' % (ALPHABETS[i], journeys[i]))
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
					j = input('Enter journey: ')
					if j.split() != []:
						journey = {
							'name': j[0].upper()+j[1:],
							'start': 0,
							'goal': 0
						}
						journeys.append(journey)
						shelf['journeys'] = journeys
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
						shelf['journeys'] = []
				else:
					# Exit application
					exit(0)
			else:
				# Exit application
				exit(0)


if __name__ == '__main__':
	main()

