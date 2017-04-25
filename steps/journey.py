from steps import calculate
from steps.constants import *
from console import align
from copy import deepcopy

def list(journeys):
	'''
	List journeys with name and goal progress
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

def add(journeys, name, goal):
	'''
	Add journey to list of journeys
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
	Clear all journeys
	'''
	return []


