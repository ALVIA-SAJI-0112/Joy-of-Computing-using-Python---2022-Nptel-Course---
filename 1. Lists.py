# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
shopping=["Bread","Coffee","Sugar"]
print(shopping)

for i in range(3):
    print(i)
    

"""
no single quotes in output
"""
for item in shopping:      
    print(item)

"""
add another item
"""
#append
shopping.append("Curd")
print(shopping)

#indexing - position holder
shopping[1]
shopping[0]

for i in range(4):
    print(shopping[i])
    
for item in shopping:
    print(item)
    
shopping[1]

shopping.append("Shampoo")
for item in shopping:
    print(item)
    
#insertion at random pos
shopping.insert(1,"Oil")
for item in shopping:
    print(item)
    
#count
ages=[12,23,34,42,15,87,12,16,25,23,82,57,7,3,2,3,1,20]
ages.count(25)
ages.count(12)
ages.count(70)

#no of elements in list
len(ages)
len(shopping)

for i in range(4):
    print(shopping[i])

for i in range(len(shopping)):
    print(shopping[i])

#sorting
ages.sort()
print(ages)

#reverse - u'll get descending order
ages.reverse()
print(ages)

students=["Arun","Rajesh","Harish","Akansha","Lakshmi","Varsha"]
students.sort()
print(students)

students.insert(0,"JOC")
print(students)

#slicing
#list_name[start:end+1]  --syntax
#list_name[start_index:end_index+1]
students[1:5]
#to get the entire list
students[:]    #default value - [0:len-1]
students

students[3:]
students[:5]
students[2:5]