from steps import calculate
from steps.constants import *
from console import align
from copy import deepcopy

def list(journeys):
	'''
	Return string of journeys with name and goal progress
	'''
	string = ''
	for i in range(len(journeys)):
		journey = journeys[i]
		journey = align.leftRight(
			'(%s) %s' % (ALPHABETS[i], journeys[i]['name']),
			'%s / %s steps' % (calculate.steps(journey['start']), journeys[i]['goal']), 
			APP_LENGTH
		)
		string += journey 
		if i != len(journeys)-1:
			string += '\n'
	return string

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
	percentage = calculate.percentage(steps, goal)
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


