# a function is a block statements which can used repectiveky in a progrsm it saves the time of a developer. in python concept off function is same in other languages

#simple function

def showdata():
    print("welcome to my profile")
showdata()
showdata()
showdata()
showdata()

#function arguments

def sum(a,b):
    print(a+b)
    
sum(20,40)
sum(20,20)

#defaults value

def sum(a,b=7):
    print(a+b)
    
sum(20)
sum(20,20)

#returns
def square(x):
    return x*x
s=square(5)
print(s)
