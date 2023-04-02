def spiral(m,n,a):
    k=0,l=0 #k=index of starting row, l=index of starting col
    while(k<m and l<n):
        #printing the 1st row from the remainng rows
        for i in range(l,n):
            print(a[k][i],end=" ")
            
        k+=1
        
        #printing the last column from the remaining column
        for i in range(k,m):
            print(a[i][n-1],end=" ")
            
        n-=1
        
        if(k<n):
            #printing the last row from remaining rows
            for i in range(n-1,l-1,-1):
                print(a[n-1],end=" ")
                
            n-=1
            
        if(l<n):
            #printing the first column from the remaining columns
            for i in range(n-1,k-1,-1):
                print(a[i][l],end=" ")
            l+=1

a=[]
for i in range(4):
    for i in range(4):
        l=[]
        for j in range(4):
            l.append(count)
            count+=1
        a.append(i)
        
spiral(4,4,a)
