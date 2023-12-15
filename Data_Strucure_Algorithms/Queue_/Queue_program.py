queue = []
def en_queue():
    element = int(input("Enter element:"))
    queue.append(element)
    print(element,"is added to the Queue")
def de_queue():
    if not queue:
        print("Queue is empty")
    else:
        e=queue.pop(0)
        print(e,"is removed from queue")
def display():
    print(queue)

while True:
    select = input("enter ur choice:1.add 2.remove 3.display 4.quit\n")
    if select=='1':
        en_queue()
    elif select=='2':
        de_queue()
    elif select=='3':
        display()
    elif select=='4':
        break
    else:
        print("invalid operation")
