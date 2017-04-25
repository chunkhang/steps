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