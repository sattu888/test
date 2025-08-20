a= (int("enter your age:"))

if(a>=18):
    print("you are enter the age of consent")
    print("good for you")

elif(a<0):
    print("you are entering an valid negative age")
elif(a==0):
    print("you are entering 0 which is not a valid consent")
else:
    print("you are below the age of consent")

print("end of program")