#iteration in different different line
l=[10,20,30,40,60,80,90]
t=len(l)
for a in range (t):
    print(l[a])
    
    for a in l:
        print(a)
        
        
        
        #reverse
        for a in range(t-1,-1,-1):
            print(l[a])
        
'''
.l[0]->10
.l[1]->20
.l[2]->30
.l[3]->40
.l[4]->60
.l[5]->80
.l[6]->90'''