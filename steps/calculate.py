import time

def now():
	'''
	Return current time in seconds
	'''
	return time.time()

def steps(start):
	'''
	Return days elapsed since start
	'''
	seconds = now() - start
	days = int(seconds // 60 // 60 // 24)
	return days

def seconds(steps):
	'''
	Return steps converted to seconds
	'''
	return steps * 24 * 60 * 60

def timestamp(t):
	''' 
	Return a tuple of formatted string of structured time 
	'''
	structuredTime = time.localtime(t)
	date = time.strftime("%d %B %Y", structuredTime)
	_time = time.strftime("%I:%M %p", structuredTime)
	return (date, _time)

def percentage(start, goal):
	'''
	Return percentage of completion
	'''
	progress = int(now() - start)
	total = seconds(goal)
	return round(progress/total * 100, 1)
