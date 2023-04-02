import random
#3 doors & a twist
doors=[]
goatdoor=[]
swap=0 #No of swap wins
dont_swap=0 #No of dont swap wins
x=random.randint(0,2) #xth door will comprise of BMW
doors[x]="BMW"
for i in range(0,3):
    if(i==x):
        continue
    else:
        door[i]="Goat"
        goatdoor.append(i)
choice=int(input("Enter your choice "))
door_open=random.choice(goatdoor) #open a door that comprises of goat
