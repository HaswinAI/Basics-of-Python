#class attributes
"""
class student():
    name="haswin"
    age=18
# getattr has three argumentes (class_name,variable,error_clear)
print(getattr(student,'age'))
print(getattr(student,'gender','no gender is identified '))

# dot notation
print(student.name)
#set attr " " "

setattr(student,"name","haswin aiml")
setattr(student,"gender","male")
student.city="selam"

print(student.name)
print(student.gender)
print(student.city)
print(student.__dict__)
#del attributes
delattr(student,"city")
print(student.__dict__)

"""

"""
class student():
    name="haswin"
    age=18

a=10
print(type(student))
print(type(a))
graduate=student()

print(isinstance(graduate,student))
print(isinstance(a,int))
print(type(graduate))

"""
#class calling
"""

class user:
    course = "python"

h=user()
print(user.__dict__)
print(user.course)
print(h.__dict__)
h.course = "c++"
print(h.__dict__)
print(h.course)
h.course

h2=user()
print(h2.course)
"""

#class method

class student:
    name="Haswin"
    age=18

    def printall():
        print("Name : ",student.name)
        print("Age : ",student.age)

student.printall()
print(student.__dict__)

print(getattr(student,"printall"))
getattr(student,"printall")




        













