import urllib2
import random
import sys
import time
import datetime


ip = sys.argv[1]
interval = int(sys.argv[2])
timerange = int(sys.argv[3])

for i in xrange(1,25):
    page = urllib2.urlopen(ip)
    sleep = interval + random.randrange(-(timerange/2), timerange/2)
    if sleep <= 0:
        sleep = 1
    print sleep
    time.sleep(sleep)