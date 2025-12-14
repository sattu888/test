course={
'python':{'duration':'6 months','fees':35000},
'html':{'duration':'5 months','fees':3000},
'java':{'duration':'3 months','fees':25000},
}

print(course)
course['java']['fees']=20000
print(course['html']['fees'])
print(course['python']['fees'])
for k,v in course.items():
    print(k,v)