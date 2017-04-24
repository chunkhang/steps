import os
import time
import shelve
from sys import exit
from steps.console import *


TITLE = '''
  ______   _________  ________  _______    ______   
.' ____ \ |  _   _  ||_   __  ||_   __ \ .' ____ \  
| (___ \_||_/ | | \_|  | |_ \_|  | |__) || (___ \_| 
 _.____`.     | |      |  _| _   |  ___/  _.____`.  
| \____) |   _| |_    _| |__/ | _| |_    | \____) | 
 \______.'  |_____|  |________||_____|    \______.' 
'''
SUBTITLE = 'A journey is simply a multitude of steps'
VERSION = '1.0.0'
WEBSITE = 'github.com/chunkhang/steps'
AUTHOR = 'MARCUS MU'
EMAIL = 'chunkhang@gmail.com'
DATA_FILE = '.data'
APP_LENGTH = 54
TITLE_LENGTH = 51
SUBTITLE_LENGTH = 42


def main():

	# Introduction
	printIntro()

	# Change working directory to script's location
	scriptPath = os.path.realpath(__file__)
	scriptDir = os.path.dirname(scriptPath)
	os.chdir(scriptDir)

	while True:

		with shelve.open(DATA_FILE) as shelf:

			# Get keys from shelf
			keys = shelf.keys()
			if len(keys) == 0:
				hasData = False
			else:
				hasData = True

			# Journeys
			printCenteredHeader('Journeys', APP_LENGTH)
			if hasData:
				for key in keys:
					print('%s: %s' % (key, shelf[key]))
			else:
				print(centerAlign('No journey found', APP_LENGTH))
			print()

			# Choices
			print()
			options = ['Add']
			if hasData:
				options.extend(['Info', 'Edit', 'Delete', 'Clear'])
			options.append('Exit')
			choice = getChoiceRows(options, 3)
			printDivider(APP_LENGTH, character='=')
			print()

			# Operations
			if choice == 0:
				# Add a journey
				print('Add a journey!')
				k = getQuery('key: ')
				v = getQuery('value: ')
				shelf[k] = v
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
					for key in keys:
						del shelf[key]
				else:
					# Exit application
					exit(0)
			else:
				# Exit application
				exit(0)


def printIntro():
	'''
	Print introduction card for application
	'''
	print(leftPad(TITLE, int((APP_LENGTH-TITLE_LENGTH)/2)))
	print(centerAlign('-'*SUBTITLE_LENGTH, APP_LENGTH))
	print(leftPad(centerAlign(SUBTITLE, SUBTITLE_LENGTH), int((APP_LENGTH-SUBTITLE_LENGTH)/2)))
	print(centerAlign('-'*SUBTITLE_LENGTH, APP_LENGTH))
	print()
	print(leftRightAlign(AUTHOR, 'VERSION %s' % VERSION, APP_LENGTH))
	print(leftRightAlign(EMAIL, WEBSITE, APP_LENGTH))
	printDivider(APP_LENGTH, character='=')
	print()

def printCenteredHeader(header, width):
	'''
	Print centered header that is lightly decorated
	'''
	string = '- %s -' % header.upper()
	print(centerAlign(string, width))
	print()

def getChoiceRows(options, numberOfRows):
	'''
	Return user choice after prompting with given rows of options
	'''
	strings = []
	for i in range(len(options)):
		strings.append('[%s] %s' % (i, options[i]))
	columns = []
	for i in range(0, len(options), numberOfRows):
		columns.append(strings[i:i+numberOfRows])
	rows = []
	for i in range(len(columns[0])):
		row = ''
		for j in range(len(columns)):
			try:
				row += columns[j][i] 
			except IndexError:
				pass
			row += '  \t'
		rows.append(row)
	for r in rows:
		print(r)
	while True:
		choice = input('\nEnter choice: ')
		if choice not in map(lambda n: str(n), range(len(options))):
			print('Invalid choice.')
		else:
			break
	return int(choice)


if __name__ == '__main__':
	main()

