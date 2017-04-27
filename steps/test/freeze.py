import time
import datetime


# Return epoch time for given datetime
def t(year, month, day, hour, minute):
	return datetime.datetime(year, month, day, hour, minute).timestamp()

# Monkey patch time.time() to return 
# 2017 April 26 4:00 pm
time.time = lambda: t(2017, 4, 26, 16, 0)