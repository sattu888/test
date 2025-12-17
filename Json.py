import json
d={
    'course_name':'python',
    'fees':15000
}
f=json.dumps(d)
print(type(f))
print(f)

# Read & write Json file in python

import.json
file=open("posts.json","r")
x=file.read()
finaldata=json.loads(x)

print(finaldata);