#default parameter function   (argument)
"""
def user(name,city="chennai"):
    print(name,"from",city)
user("haswin","nammakal")
"""
#using list as the argument in the function
#we can call the list directly to function 
"""
def student(marks):
    return sum(marks)

print(student([100,80,90,70,54]))
"""

#recurtion function(call itself)
"""
def factorial(x):
    #pass  can avoid error
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))

print("the factorial is : ",factorial(7))
"""
#lambda function
"""
c= lambda a:a+100
print(c(5))

c=lambda a,b:a+b
print(c(10,25))
"""
