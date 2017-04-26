import sys; sys.path.append('../steps')
from freeze import *
from steps import calculate


def test_now():
	assert calculate.now() == t(2017, 4, 26, 16, 0)

def test_steps_exactly_six_days():
	assert calculate.steps(t(2017, 4, 20, 16, 0)) == 6

def test_steps_almost_six_days():
	assert calculate.steps(t(2017, 4, 20, 16, 1)) == 5

def test_seconds():
	assert calculate.seconds(365) == 31536000

def test_timestamp():
	date, time = calculate.timestamp(t(2015, 3, 10, 20, 38))
	assert date == '10 March 2015'
	assert time == '08:38 PM'

def test_percentage_50():
	assert calculate.percentage(t(2017, 4, 25, 16, 0), 2) == 50.0

def test_percentage_exceed_100():
	assert calculate.percentage(t(2017, 4, 23, 16, 0), 2) == 100.0

