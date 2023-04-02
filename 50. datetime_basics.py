# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 21:34:36 2022

@author: alvia
"""
#console
#current time
from datetime import datetime as dt
import datetime
from datetime import datetime as dt
dt.now()
print(dt.now())
import pytz
tz=pytz.timezone('Singapore')
print(dt.now(tz))
pytz.all_timezones
len(pytz.all_timezones)

#given date, determine day
import calendar
calendar.weekday?
calendar.weekday(2018,7,6)




