color = input("enter signal color:")

if color=='green':
    print("car can go")
elif color=='yellow':
    print("car should wait")
elif color=='red':
    print("car stop")
else:
    print("traffic error")