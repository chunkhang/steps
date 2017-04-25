def left(text, width):
	''' Return a string left-aligned within the given width '''
	words = text.split()
	# Check longest word against width
	longestWord = ''
	for word in words:
		if len(word) > len(longestWord):
			longestWord = word
	assert len(longestWord) <= width, 'Longest word cannot exceed width.'
	# Left-align text
	string = ''
	line = ''
	firstWord = True
	for word in words:
		lineLength = len(line)
		wordLength = len(word) + 1
		if firstWord:
			line += word
			firstWord = False
			continue
		if lineLength + wordLength > width:
			line += ('\n')
			string += line
			line = word
		else:
			line += (' ' + word)
	string += line
	return string

def center(text, width):
	''' Return a string centered-aligned within the given width '''
	leftAlignedText = left(text, width)
	lines = leftAlignedText.split('\n')
	centeredLines = list(map(lambda line: line.center(width), lines))
	return '\n'.join(centeredLines)

def leftRight(left, right, width):
	''' Return a string that left aligns left and right aligns right within the given width'''
	length = width - len(left) - len(right)
	string = '%s%s%s' % (left, ' '*length, right)
	return string

def leftPad(text, padding):
	''' Return a string left-padded with the given padding '''
	lines = text.split('\n')
	paddedLines = (map(lambda line: ' '*padding + line, lines))
	return '\n'.join(paddedLines)