import time

def now():
	'''
	Return current timestamp
	'''
	return time.time()

def steps(start):
	'''
	Return days elapsed since start
	'''
	seconds = now() - start
	days = int(seconds // 60 // 60 // 24)
	return days

def timestamp(t):
	''' 
	Return a tuple of formatted string of structured time 
	'''
	structuredTime = time.localtime(t)
	date = time.strftime("%d %B %Y", structuredTime)
	_time = time.strftime("%I:%M %p", structuredTime)
	return (date, _time)

def percentage(x, y):
	'''
	Return percentage of x over y
	'''
	return round(x/y * 100, 1)