#to read a file
with open("file1.txt") as myfile:
    print(myfile.read())

#to write a file
with open("file1.txt","w") as myfile:
    myfile.write("I am fine")
myfile.close()

#to read and write a file
with open("file1.txt","r+") as myfile: #opens the file in read as well as write mode
    print(myfile.read())
    myfile.write("I am fine")
myfile.close()

"""
modes in which u can open a file
r-read
w-write
a-append
r+read and write simultaneouldy
"""