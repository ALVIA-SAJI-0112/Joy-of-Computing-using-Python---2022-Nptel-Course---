x=[4,3,1,2]
print(sorted(x))
print(sorted(x,reverse=True))
x=['q','w','e','r','t','y']
print(sorted(x))
x='python'
print(sorted(x))
x={'q':1,'w':2,'e':4,'t':0}
print(sorted(x))
L=["ccccc","bb","a","ddd"]
print(sorted(L,key=len))


str1=input("Enter the 1st string")
str2=input("Enter the 2nd string")
print(sorted(str1))
print(sorted(str2))
if(sorted(str1)==sorted(str2)):
    print("These are Anagrams")
else:
    print("These are not Anagrams")
    