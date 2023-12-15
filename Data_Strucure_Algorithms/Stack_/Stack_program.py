stack = []
def push_element():
    element = int(input("Enter element:"))
    stack.append(element)
    print(element,"is added to the stack")
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print(e,"is removed from stack")
def top_element():
    top=stack[-1]
    print("top element is ",top)
def display():
    print(stack)

while True:
    select = input("enter ur choice:1.push 2.pop 3.top 4.display 5.quit\n")
    if select=='1':
        push_element()
    elif select=='2':
        pop_element()
    elif select=='3':
        top_element()
    elif select=='4':
        display()
    elif select=='5':
        break
    else:
        print("invalid operation")
