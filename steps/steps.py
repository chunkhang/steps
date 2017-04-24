from steps.console import *


TITLE = '''
  ______   _________  ________  _______    ______   
.' ____ \ |  _   _  ||_   __  ||_   __ \ .' ____ \  
| (___ \_||_/ | | \_|  | |_ \_|  | |__) || (___ \_| 
 _.____`.     | |      |  _| _   |  ___/  _.____`.  
| \____) |   _| |_    _| |__/ | _| |_    | \____) | 
 \______.'  |_____|  |________||_____|    \______.' 
'''
SUBTITLE = 'A console application for tracking the progress of curbing bad habits'
VERSION = '1.0.0'
WEBSITE = 'github.com/chunkhang/steps'
AUTHOR = 'MARCUS MU'
EMAIL = 'chunkhang@gmail.com'
APP_LENGTH = 60
TITLE_LENGTH = 51
SUBTITLE_LENGTH = 42


def main():
	printIntro()
	printCenteredHeader('Hello', APP_LENGTH)
	print('h')


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


if __name__ == '__main__':
	main()








