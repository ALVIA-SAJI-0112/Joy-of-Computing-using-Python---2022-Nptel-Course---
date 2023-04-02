"""
crowd computing
overestimation - underestimation = 0
10% trimmed mean - removing 10% of largest and smallest values
    sort the values
    calc mean
collective opinion > expert opinion
wikipedia - crowd sourced
britannica - curated by experts
"""
Estimates = [1000,1010,1786, 2000,1500,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
Estimates.sort()  #to sort the list
for i in range(len(Estimates)):
    print(Estimates[i])
    
#trimvalue
tv=(0.1*len(Estimates))
Estimates=Estimates[tv:]
for i in range(len(Estimates)):
    print(Estimates[i])
    
#remove tvs
from statistics import mean
Estimates = [1000,1010,1786, 2000,1500,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
Estimates.sort()
tv=(0.1*len(Estimates))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]
print(mean(Estimates))
    
#easier way to calculate trim mean
from scipy import stats
from statistics import mean
Estimates = [1000,1010,1786, 2000,1500,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
Estimates.sort()
m = stats.trim_mean(Estimates,0.1)
print(m)
#tv=(0.1*len(Estimates))
#Estimates=Estimates[tv:]
#Estimates=Estimates[:len(Estimates)-tv]
#print(mean(Estimates))

import matplotlib.pyplot as plt
import statistics
Estimates=[1000,1010,1786,2000,1500,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
"""
python generates x values
here, we storing range of values in x
and keeping y values constant 
"""
y=[1000,1010,1786,2000,1500,100,120,150,150,170,175,18.....]
Estimates.sort()
tv=int(0.1*(len(Estimates)))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates-tv)]
for i in range(len(Estimates)):
    y.append(5)  #appending any constant  (y axis value is constant)
plt.plot([Estimates],y,'r--') #estimates in x axis and 5 in y axis (usually automatically a list would be taken in y axis and x is generated auto. but there we are explicitly assigning x axis to be estimates)
plt.plot([statistics.mean(Estimates)],[5],'ro') 
plt.plot([statistics.median(Estimates)],[5],'bs') 
plt.plot([375],[5],'g^') 