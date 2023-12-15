""" Sort a Stack"""
def createStack(): # Creating stack
    stack = []
    return stack

def isEmpty( stack ): # check stack empty
    return len(stack) == 0

def push( stack, item ): # push items to stack
    stack.append( item )

def top( stack ): # to get top item of stack
    p = len(stack)
    return stack[p-1]

def pop(stack): # pop stack item
    if (isEmpty(stack)):
        return "empty"
    return stack.pop()

def prints(stack): # print stack
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end = ' ')
    print()


def sortStack ( stack ): #sorting
    tmpStack = createStack()
    #print(tmpStack)
    while(isEmpty(stack) == False):
        tmp = top(stack)
        pop(stack)
        while (isEmpty(tmpStack) == False and int(top(tmpStack)) < int(tmp)):
            push(stack, top(tmpStack))
            pop(tmpStack)
        push(tmpStack, tmp)
    return tmpStack



stack = createStack()
push( stack, str(34) )
push( stack, str(3) )
push( stack, str(31) )
push( stack, str(98) )
push( stack, str(92) )
push( stack, str(23) )
print(prints(stack))
print("Sorted numbers are: ")
sorted_stack = sortStack ( stack )
prints(sorted_stack)
#print("Popped item:" + pop(stack))
#print("Stack after popping an element :" + str(stack))
#print(prints(stack))

