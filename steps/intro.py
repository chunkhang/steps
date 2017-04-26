from steps.console import align
from steps.constants import *

def printIntro():
	'''
	Print introduction card for application
	'''
	print(align.leftPad(TITLE, int((APP_LENGTH-TITLE_LENGTH)/2)))
	print(align.center('-'*SUBTITLE_LENGTH, APP_LENGTH))
	print(align.leftPad(align.center(SUBTITLE, SUBTITLE_LENGTH), int((APP_LENGTH-SUBTITLE_LENGTH)/2)))
	print(align.center('-'*SUBTITLE_LENGTH, APP_LENGTH))
	print()
	print(align.leftRight(AUTHOR, 'VERSION %s' % VERSION, APP_LENGTH))
	print(align.leftRight(EMAIL, WEBSITE, APP_LENGTH))