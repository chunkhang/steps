import sys; sys.path.append('../steps')
from freeze import *
from copy import deepcopy
from steps import journey


class Mock:
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


def test_list():
	original = deepcopy(Mock.journeys)
	list = journey.list(Mock.journeys)
	left, right = list
	assert left == ['(A) First', '(B) Second']
	assert right == ['1 / 100 steps', '1 / 200 steps']
	assert Mock.journeys == original

def test_details():
	original = deepcopy(Mock.journeys)
	assert journey.details(Mock.journeys, 0) == \
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
	assert journey.details(Mock.journeys, 1) == \
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
	assert Mock.journeys == original

def test_add():
	original = deepcopy(Mock.journeys)
	journey.add(Mock.journeys, 'Third', 300)
	assert Mock.journeys == original
	assert journey.add(Mock.journeys, 'Third', 300) == [
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
	original = deepcopy(Mock.journeys)
	journey.clear()	
	assert Mock.journeys == original
	assert journey.clear() == []
