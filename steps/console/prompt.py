from steps.console import align

def choice(numbers, choices, prompt='\nEnter choice: ', error='Invalid choice.'):
	'''
	Prompt user for choice
	Return an integer of valid choice
	'''
	assert len(numbers) == len(choices), 'Length of list of numbers and list of choices must be the same.'
	assert all(type(number) == int for number in numbers), 'Numbers must be integer.'
	assert all(type(choice) == str for choice in choices), 'Choices must be string.'
	for i in range(len(numbers)):
		print('[%s] %s' % (numbers[i], choices[i]))
	while True:
		choice = input(prompt)
		try:
			choice = int(choice)
			if choice in numbers:
				return choice
			else:
				raise ValueError()
		except ValueError:
			print(error)

def choiceRows(options, numberOfRows):
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
	
def query(prompt='\nEnter query: ', error='Invalid query.'):
	''' 
	Prompt user for query
	Return a string of valid query 
	'''
	while True:
		q = input(prompt)
		if q != '':
			return q
		else:
			print(error)

def yesOrNo(prompt='\nEnter response (Y/N) ', error='Invalid response.'):
	'''
	Prompt user for yes or no
	Return a string of either 'Y' or 'N'
	'''
	while True:
		response = query(prompt, error)
		if response.upper() in 'Y N'.split():
			return response.upper()
		else:
			print(error)

def enter(action='continue'):
	''' 
	Prompt user to hit enter 
	'''
	input('[Hit enter to %s]' % action)

def enterCenter(width, action='continue'):
	'''
	Prompt user to hit enter with a centered text within the given width
	'''
	input(align.center('[Hit enter to %s]' % action, width))
