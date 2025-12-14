l=[]
while True:
    c=int(input ('''
        1 push elements
        2 pop elements
        peek elements
        display Stack
        exit
        '''))
    
#push elements
if c==1:
    n=input("enter the value");
    l.append(n)
    print(l)
    
    #pop elements
if c==2:
    if len(l)==0:
        print("empty list")
else:
    p=l.pop()
    print(p)
    print(l)
    
    
#peak elements

elif
    c==3:
    if len(l)==0:
        print("empty stack")
    else:
        print("last stack")