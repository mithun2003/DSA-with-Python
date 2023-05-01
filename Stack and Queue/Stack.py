class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Stack:
    def __init__(self,head=None):
        self.top = head
    def display(self):
        node = self.top
        if node is None:
            print("EMPTY")
        else:
            while node is not None:
                print(node.data,end=" ")
                node = node.next 
    def push(self,data):
        node = self.top
        temp = Node(data)
        if node is None:
            self.top=temp
        else:
            temp.next =self.top
            self.top=temp
    def pop(self):
        node = self.top
        if node is None:
            print("Empty")
        else:
            self.top = self.top.next    
    
stack = Stack()
arr=[5,4,3,2,1]
for i in arr:
    stack.push(i)
stack.display()
stack.pop()
stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
print()
stack.display()