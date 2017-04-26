import time
import sys; sys.path.append('../steps')
from steps import calculate

# Monkey patch time.time() to return 
# Wed 26 Apr 4:05 pm
def freezeTime():
	return 1493193914.75961
time.time = freezeTime

def test_now_basic():
	assert calculate.now() == 1493193914.75961



