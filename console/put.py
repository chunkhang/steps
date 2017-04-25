from console.align import *

def title(title, width, character='*', padding=1):
	''' Print a decorated title '''
	assert type(title) == str and title != '', 'Title must be non-empty string.'
	assert type(width) == int and width >= len(title), 'Width must be at integer that is at least length of title.'
	assert type(character) == str and len(character) == 1, 'Character must be string of length 1.'
	assert type(padding) == int and padding >= 1, 'Padding must be integer that is at least 1.'
	length = len(title)
	string = center(character*(length + padding*4), width)
	string += '\n'
	titleString = center('%s%s%s' % (' '*(padding*2 - 1), title, ' '*(padding*2 - 1)), width)
	firstIndex = 0
	for char in titleString:
		if char != ' ':
			firstIndex = titleString.index(char) - padding*2
			break
	lastIndex = firstIndex + length + padding*4
	titleString = titleString[:firstIndex] + character + titleString[firstIndex+1:lastIndex-1] + character + titleString[lastIndex:]
	string += titleString
	string += '\n'
	string += center(character*(length + padding*4), width)
	print(string)

def header(header, character='=', padding=1, newLineBelow=True):
	''' Print a decorated header '''
	assert type(character) == str and len(character) == 1, 'Character must be string of length 1.'
	print(' '*padding + header)
	print(character*(len(header)+ padding*2))
	if newLineBelow:
		print()

def headerCenter(header, width, newLineBelow=True):
	'''
	Print centered header that is lightly decorated
	'''
	string = '- %s -' % header.upper()
	print(center(string, width))
	if newLineBelow:
		print()
	
def divider(length, character='-', newLineAbove=True):
	''' Print a horizontal divider '''
	assert type(character) == str and len(character) == 1, 'Character must be string of length 1.'
	divider = character*length
	if newLineAbove:
		divider = '\n' + divider
	print(divider)	