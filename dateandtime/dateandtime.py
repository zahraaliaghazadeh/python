# import time
#
# print("The epoch on this system starts at" + time.strftime("%c", time.gmtime(0)))
#
# print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\t Daylight saving Time is in effect for this location" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#     print("\t The DST timezone is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
#
#

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

# the problem with time and timezon, on youtube