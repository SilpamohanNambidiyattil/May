""" Working of Stack
            1. A pointer called TOP is used to keep track of the top element in the stack.

            2. When initializing the stack, we set its value to -1 so that we can check if the stack is empty
             by comparing TOP == -1.

            3. On pushing an element, we increase the value of TOP and place
            the new element in the position pointed to by TOP.

            4. On popping an element, we return the element pointed to by TOP and reduce its value.

            5. Before pushing, we check if the stack is already full

            6. Before popping, we check if the stack is already empty  """

# Creating a Stack
def create_stack():
    stack = []
    return stack

# Creating an empty Stack
def check_empty(stack):
    return len(stack)==0

# Adding items into the stack
def push(stack, items):
    stack.append(items)
    print("pushed items :" + items)

# Removing an element from stack
def pop(stack):
    if (check_empty(stack)):
        return "empty"
    return stack.pop()

def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end = ' ')
    #return
    print()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
print(prints(stack))
print("Popped item:" + pop(stack))
print("Stack after popping an element :" + str(stack))
