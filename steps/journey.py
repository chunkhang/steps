from steps import calculate
from steps.constants import *
from steps.console import align
from copy import deepcopy

def list(journeys):
	'''
	Return a tuple of two lists of strings for name and steps respectively
	'''
	left = []
	right = []
	for i in range(len(journeys)):
		journey = journeys[i]
		left.append('(%s) %s' % (ALPHABETS[i], journeys[i]['name']))
		right.append('%s / %s steps' % (calculate.steps(journey['start']), journeys[i]['goal']))
	return (left, right)

def details(journeys, index):
	'''
	Return string of journey details
	'''
	journey = journeys[index]
	name = journey['name']
	start = journey['start']
	startDate, startTime = calculate.timestamp(start)
	goal = journey['goal']
	steps = calculate.steps(start)
	now = calculate.now()
	nowDate, nowTime = calculate.timestamp(now)
	percentage = calculate.percentage(start, goal)
	string = 'JOURNEY\n'
	string += '-------\n'
	string += '%s\n' % name
	string += '\n'
	string += 'START\n'
	string += '-----\n'
	string += '%s\n' % startDate 
	string += '%s\n' % startTime
	string += '\n'
	string += 'TODAY\n'
	string += '-----\n'
	string += '%s\n' % nowDate
	string += '%s\n' % nowTime
	string += '\n'
	string += 'STEPS\n'
	string += '-----\n'
	string += '%s out of %s\n' % (steps, goal)
	string += '\n'
	string += 'PROGRESS\n'
	string += '--------\n'
	string += '%s %%' % percentage
	return string

def add(journeys, name, goal):
	'''
	Return list of journeys with added journey
	'''
	journey = {
		'name': name[0].upper() + name[1:],
		'start': calculate.now(),
		'goal': goal
	}
	journeysCopy = deepcopy(journeys)
	journeysCopy.append(journey)
	return journeysCopy

def clear():
	'''
	Return empty list
	'''
	return []


