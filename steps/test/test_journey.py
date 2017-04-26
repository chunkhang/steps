import sys; sys.path.append('../steps')
from freeze import *
from copy import deepcopy
from steps import journey


def test_list():
	journeys = [
		{
			'name': 'First',
			'start': t(2017, 4, 25, 16, 0),
			'goal': 100
		},
		{
			'name': 'Second',
			'start': t(2017, 4, 25, 16, 0),
			'goal': 200
		}
	]
	original = deepcopy(journeys)
	list = journey.list(journeys)
	left, right = list
	assert left == ['(A) First', '(B) Second']
	assert right == ['1 / 100 steps', '1 / 200 steps']
	assert journeys == original

def test_details():
	journeys = [
		{
			'name': 'First',
			'start': t(2017, 4, 25, 16, 0),
			'goal': 100
		},
		{
			'name': 'Second',
			'start': t(2017, 4, 25, 16, 0),
			'goal': 200
		}
	]
	original = deepcopy(journeys)
	assert journey.details(journeys, 0) == \
'''\
JOURNEY
-------
First

START
-----
25 April 2017
04:00 PM

TODAY
-----
26 April 2017
04:00 PM

STEPS
-----
1 out of 100

PROGRESS
--------
1.0 %\
'''
	assert journey.details(journeys, 1) == \
'''\
JOURNEY
-------
Second

START
-----
25 April 2017
04:00 PM

TODAY
-----
26 April 2017
04:00 PM

STEPS
-----
1 out of 200

PROGRESS
--------
0.5 %\
'''
	assert journeys == original

def test_add():
	journeys = [
		{
			'name': 'First',
			'start': t(2017, 4, 25, 16, 0),
			'goal': 100
		},
		{
			'name': 'Second',
			'start': t(2017, 4, 25, 16, 0),
			'goal': 200
		}
	]
	original = deepcopy(journeys)
	journey.add(journeys, 'Third', 300)
	assert journeys == original
	assert journey.add(journeys, 'Third', 300) == [
		{
			'name': 'First',
			'start': t(2017, 4, 25, 16, 0),
			'goal': 100
		},
		{
			'name': 'Second',
			'start': t(2017, 4, 25, 16, 0),
			'goal': 200
		},
		{
			'name': 'Third',
			'start': t(2017, 4, 26, 16, 0),
			'goal': 300
		}
	]

def test_clear():
	journeys = [
		{
			'name': 'First',
			'start': t(2017, 4, 25, 16, 0),
			'goal': 100
		},
		{
			'name': 'Second',
			'start': t(2017, 4, 25, 16, 0),
			'goal': 200
		}
	]
	original = deepcopy(journeys)
	journey.clear()	
	assert journeys == original
	assert journey.clear() == []
