import time
import datetime


# Monkey patch time.time() to return 
# Wed 26 Apr 2017 4:00 pm
def freezeTime():
	return t(2017, 4, 26, 16, 0)
time.time = freezeTime

# Return epoch time for given datetime
def t(year, month, day, hour, minute):
	return datetime.datetime(year, month, day, hour, minute).timestamp()