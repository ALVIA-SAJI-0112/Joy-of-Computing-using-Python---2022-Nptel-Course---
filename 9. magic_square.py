"""
magic square
n - size of matrix
magic number, M=n((n^2)+1)/2 - magic number
patterns observed in magic squares
1. pos of 1 is in the middle row and last col..(r,c)=(n/2,n-1)
2. lets say the pos of 1 i.e. (n/2,n-1) is (p,q), then next number which is 2 is located at (p-1,q+1) position.
Anytime if the calculated row position becomes -1 then make it n-1 and if col pos becomes n then make it 0.
3. If the calculated pos already contains a number then decrement the col by 2 and increment the row by 1.
4. If anytime row pos becomes -1 and col becomes n, switch it to (0,n-2)



x   x   x
00  01  02

x   x   x
10  11  12

x   x   x
20  21  22
Steps:
N=3
1. Postion of 1: (3/2,3-1)=(1,2)
2. Postion of 2: (1-1,2+1)=(0,3)=(0,0)
3. Postion of 3: (0-1,0+1)=(-1,1)=(3-1,1)=(2,1)
4. Postion of 4: (2-1,1+1)=(1,2)
Since 1 is present at this position, apply 2nd condition = (1+1,2-2)=(2,0)
5. Postion of 5: (2-1,0+1)=(1,1)
6. Postion of 6: (1-1,1+1)=(0,2)
7. Postion of 7: (0-1,2+1)=(-1,3)
Condition 3: (0,1)
6. Postion of 8: (0-1,1+1)=(-1,2)=(2,2)
7. Postion of 9: (2-1,2+1)=(1,3)=(1,0)
"""

"""
magic=[0 for i in range(3)]
magic

magic=[[0 for i in range(3)] for j in range(3)]
magic
"""

"""
def magic_square(n):
    
    
    magicSquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
 
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()
magic_square(3)
"""

#program starts here
def magic_square(n):
    
    
    magicSquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
        i=n//2
        j=n-1
        
        num=n*n
        count=1
        
        while(count<=num):
            if(1==-1 and j==n): #Condition 4
                j=n-2
                i=0
            else:
                if(j==n):
                    j=0
                if(i<0):  #row is becoming -1
                    i=n-1
            if(magicSquare[i][j]!=0):
                j=j-2
                i=i+1
                continue
            
            else:
                magicSquare[i][j]=count
                count+=1
                
            i=i-1
            j=j-1 #Condition 1
        
            
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()
        
    print("The sum of each row/column/diagonal is: "+str(n*(n**2+1))/2)
magic_square(3)

