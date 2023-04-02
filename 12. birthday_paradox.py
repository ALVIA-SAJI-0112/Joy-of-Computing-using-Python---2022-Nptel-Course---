"""
If month is Februray and year is lleap year then
Generate day randomly from 1 to 29
if month is February and year is not a leap year then
Generate day randomly from 1 to 28
If month%2==0 and month>7 then //April and June
Generate day randomly from 1 to 30
If month%2==0 and month>7 then //August, October and December
Generate day randomly from 1 to 31
If month%2!=0 and month<7 then //January, March, July
Generate day randomly from 1 to 31
If month%2!=0 and month<7 then //September and November
Generate day randomly from 1 to 3o
"""
#datetime function
datetime.date.today()
datetime.date.today().strftime("%Y")
datetime.date.today().strftime("%B")
datetime.date.today().strftime("%d")
print("Week number of the month",datetime.date.today().strftime("%W"))
print("Weekday of the month",datetime.date.today().strftime("%w"))
print("Day of year",datetime.date.today().strftime("%j"))
print("Day of week",datetime.date.today().strftime("%A"))
print("Day time",datetime.now()


#program starts here
import random
import datetime
birthday=[]
i=0
while(i<50):
    year=random.randint(1895,2017)
#The oldest person ever lived was 122 years old
    if(year%4==0 and year%100!=0  or year%400==0):
        leap=1
    else:
        Leap=0
    month=random.randint(1,12)
    if(month==2 and leap==1):
        day=random.randint(1,29)
    elif(month==2 and leap==0):
        day=random.randint(1,29)
    elif(month==7 or month==8):
        day=random.randint(1,31)
    elif(month%4==0 and month>7 and month<12):
        day=random.randint(1,31)
    else:
        day=random.randint(1,30)  
    dd=datetime.date(year,month,day)
    day_of_year=dd.timetuple().tm_yday
    i=i+1
    birthday.append(day_of_year)
    
birthday.sort()
i=0
while(i<50):
    print(birthday[i])
    i+=1