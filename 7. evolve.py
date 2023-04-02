import random

def evolve(x):
    ind=random.randint(0,len(x)-1) #to generate a random index in the list x
    p=random.randint(1,100)
    print(p)
    if(p==1):
        if(x[ind]=='0'):
            x[ind]=='1'
        else:
            x[ind]=='0'

with open("dna_data.txt") as myfile:
    x=myfile.read()
    x=list(x) #converting it to list
    
for i in range(0,10000): #here are 10,000 bits given in the file #no of times evolution to be performed
    evolve(x)
print(x)


#Assignment 3
L = ["Practice", "makes", "the", "man", "perfect. "]
L.sort()
for element in L:
      print(element)


#What is the correct code for a function to return the sum of elements of list L?
   def sum of_list(L):
         Total = 0
         for i in range(len(L)):
              Total = Total + L[i]
         return Total
     
L = [1,2,3,4,5,6,7,8,9,10]
total_sum=sum_of_list(L)
print(total_sum)

'''
You are given a list named L. Print all the elements at odd position of list L.(We will take care of the input, you just have to print elements present at odd position)

Input:

A List L

Output 

All elements present at odd position

'''
L = [int(i) for i in input().split()]
for i in range(len(L)):
    if(i%2!=0):
        print(L[i])
        
        
'''
You are given a list L. Print the list of first 3 smallest elements in ascending order and last 2 greatest elements in descending order of the list L respectively.(We will take care of the input)

Input: A list L
Output:
A list of first 3 smallest elements in L in ascending order
A list of last 2 greatest elements in L in descending order
'''
L = [int(i) for i in input().split()]
L.sort()
print(L[0:3])
L.reverse()
print(L[0:2])




'''
You are given a list L. Write a function all_even that accepts the list L and print all the even numbers is the list L.(Order of the numbers should be same as the order present in the list)

We will take care of the input.
Input: A list L
Output:
all the even numbers in list
'''
def all_even(L):
    for i in L:
        if i%2 == 0:
            print(i)
L = [int(i) for i in input().split()]
all_even(L)