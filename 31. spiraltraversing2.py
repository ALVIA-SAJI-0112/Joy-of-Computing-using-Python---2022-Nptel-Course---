import turtle
turtle.bgcolor("black")
seurat=tutle.Turtle()
from random import randint

width=5
height=7
dot_distance=25

seurat.penup()
list_color=["white","yellow","brown","red","blue","green","orange","pink","violet","grey"]
seurat.setpos(-250,250)

def spiralPrint(m,n):
    k=0,l=0 #k=index of starting row, l=index of starting col
    f=0
    col=randint(0,10)
    seurat.color(list_color[col])
    
    while(k<m and l<n):
        if(f==1):
            seurat.right(90)
        #printing the 1st row from the remainng rows
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[k][i],end=" ")
            
        k+=1
        f=1
        
        seurat.right(90)
        #printing the last column from the remaining column
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[i][n-1],end=" ")
            
        n-=1
        
        if(k<n):
            #printing the last row from remaining rows
            for i in range(n-1,(l-1),-1):
                print(a[n-1],end=" ")
                
            m-=1
        seurat.right(90)
        if(l<n):
            #printing the first column from the remaining columns
            for i in range(n-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[i][l],end=" ")
            l+=1


        
R=C=20
spiralPrint(R,C)
turtle.done()
