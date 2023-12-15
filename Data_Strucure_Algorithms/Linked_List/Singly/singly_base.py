
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class linked_list:
    def __init__(self):
        self.head = None
    def print_ll(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n= self.head
            while n is not None:
                print(n.data, "--->", end='')
                n= n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n = self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def add_bet(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("item not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def del_begin(self):
        if self.head is None:
            print("Empty")
        else:
            self.head=self.head.ref
    def del_end(self):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def del_value(self,x):
        if self.head is None:
            print("Empty")
            return
        if x== self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            n.ref=n.ref.ref




ll = linked_list()
ll.add_begin(10)
ll.add_begin(20)
ll.add_begin(30)
ll.add_end(100)
ll.add_bet(200,20)
#ll.del_begin()
#ll.del_end()
#ll.del_value(10)
ll.print_ll()