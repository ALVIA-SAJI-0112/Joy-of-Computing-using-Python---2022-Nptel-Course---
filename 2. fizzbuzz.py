# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 08:53:41 2022

@author: alvia
"""
for i in range(50):
    print(i)
    
for i in range(1,51):
    print(i)

#create a function and call it
def fizzbuzz(r):
    for i in range(1,51):
        if(i%3==0 and i%5==0):
                print(str(i)+" = FizzBuzz")
        else:
            if(i%3==0):
                print(str(i)+" = Fizz") 
            else:
                if(i%5==0):
                    print(str(i)+" = Buzz")  
                else:
                    print(str(i))                   
fizzbuzz(51)

#typecast to str
x=1324
str(x)
a=str(x)
a[2]