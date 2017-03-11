'''
Jenny Tso
Python Datetime Drill

'''

from datetime import datetime
from pytz import timezone
import pytz

time_Portland = datetime.now(pytz.timezone('US/Pacific'))
time_str = time_Portland.strftime('%H:%M')
time_NY = datetime.now(pytz.timezone('US/Eastern'))
time_London = datetime.now(pytz.timezone('Europe/London'))

def openOrClosed():
    if (time_Portland.hour >= 9) and (time_Portland.hour <= 21):
        print "The Portland office is open."
    else:
        print "The Portland office is closed."

    if (time_NY.hour >= 9) and (time_NY.hour <= 21):
        print "The NY office is open."
    else:
        print "The NY office is closed."

    if (time_London.hour >= 9) and (time_London.hour <= 21):
        print "The London office is open."
    else:
        print "The London office is closed."

print ("The current time in Portland is " + time_str + ".\n")
openOrClosed()
print "\n**Have a nice day!**"
