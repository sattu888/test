#function for element from list-
#insert()
l=[20,30,50,60]
l.insert(1,40)
l.insert(5,100)
print(l)

#append() add in last element
l=[20,30,50,60]
n=[40,50]
l.append(10)
l.append(n)
print(l)

#extends() Works on the value inside
l=[20,30,50,60]
n=[40,50]
l.extend(n)
print(l)