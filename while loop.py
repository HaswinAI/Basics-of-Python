#while continue
"""
i=1
while i<=20:
    if i%2==0:
        i=i+1
        continue;
    print(i)
    i+=1
"""
#while break
"""
i=1
while i<=20:
    if i==7:
        break;
    print(i)
    i+=1
"""
"""
a=list(range(0,21,5))
print(a)
"""
#for loop
"""
for i in range(5):
    a=int(input("enter the num1 : "))
    b=int(input("enter the num2 : "))
    i=a+b
    print(i)
"""
#star patten
"""
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="") # end used for make the statement in single line.
    print("")
"""
#huskey keeys A-Z=>65-98
# a-z = > 97-122

for i in range (65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("haswin")
 