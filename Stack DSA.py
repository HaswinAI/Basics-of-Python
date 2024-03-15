top = 0
mymax=eval(input("enter maximum sixe of the stack "))
def createstack():
    stack=[]
    return stack
def isempty(stack):
    return len(stack)==0
def push(stack,item):
    print("pushed to stack")
def pop(stack):
    if isempty(stack):
        return "stack underflow"
    return stack.pop()
stack=createstack()
while True:
    print("1.push")
    print("2.pop")
    print("3.display")
    print("4.quick")
    ch=int(input("enter your choice : "))
    if ch==1:
        if top<mymax:
            item=input("enter any element :")
            push(stack.item)
            top+=1
        else:
            print("stack overflow")
    elif ch==2:
        print(pop(stack))
    elif ch==3:
        print(stack)
    else:
        print("exit")
        break
