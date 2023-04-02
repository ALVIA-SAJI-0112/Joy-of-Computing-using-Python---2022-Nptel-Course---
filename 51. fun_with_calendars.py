# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 21:46:58 2022

@author: alvia
"""

def check_valid_date(dt,m,y,l):
    if l:
        if m==2:
            if dt<30:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2==1:
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False
            else:
                if m%2==0:
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False
    else:
        if m==2:
            if dt<30:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2==1:
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False
                else:
                    if m%2==0:
                        if dt<32:
                            return True
                        else:
                            return False
                    else:
                        if dt<31:
                            return True
                        else:
                            return False
                    
                    
def get_day:
    list_of_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] 
    return list_of_days[days_index] 

     
def check_leap(y):
    if y%100==0:
        if y%400==0:
            return True
        else:
            return False
    else:
        if y%4==0:
            return True
        else:
            return False
        
while(1):
    year=int(input('Enter year(1970-2018):'))
    if year<1917:
        print('Enter a year in the range 1970')
    else:
        break
    
while(1):
    year=int(input('Enter month(1-12):'))
    if month<=12 and month>0:
        break
    else:
        print('Enter a valid month (1-12)')
    
leap=check_leap(year)
while(1):
    date=int(input('Enter date: '))
    if date>0 and check_valid_date(date,month,year,leap):
        break
    else:
        print('Enter a valid date)')
 
    
day_index=calendar.weekday(year,month,day)
day=get_day(day_index)
ptrint(date,"/",month,"/",year,"falls on",day)
check_leap(year)




from datetime import datetime as dt
import pytz
timezonnes=pytz.all_timezones
for i in range(len(timezones)):
    zone=timezones[i]
    tz=pytz.timezone(zone)
    print("Curent time at zone",zone,"is",st.now(tz))
    