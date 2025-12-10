l=[]
for a in range(1,101):
    #print(a)
    l.append(a)
    
    print(l)
    
    #comprehension use
    
n=[m for m in range(1,1000)]
n=[h for h in range(1,101) if h%2==0]
print(n)