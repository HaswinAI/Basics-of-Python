#list->[]
"""
none notes
"""

#tuplt->()
"""
a=(1,2,3,4)
b=(5,6,7,8)
c=(a,b)
print(c)
"""

#sets->{}
"""
name={"ravi","ram","haswin"}
print(type(name))
"""
#for in sets
"""
for names in name:
    print(names)
"""
#udating and deleting sets
"""
a={"ravi","jalastine","gokul"}
name.update(a)
print(name)
name.remove("gokul")
print(name)
name.discard("haswi")
print(name)

name={"ravi","ram","haswin"}
del name
print(name)
"""
#union and update

a={1,2,3,4}
b={'a','b','c','d'}
c=a.union(b)
a.update(b)
print(a) 
