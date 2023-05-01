class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Dlinkedlist():
    def __init__(self, head=None):
        self.head = head

    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
    #INSERT AT START
    def insert_at_start(self, data):
        temp = Node(data)
        if self.head is not None:
            self.head.prev = temp
        temp.next = self.head
        self.head = temp
    #INSERT AT END
    def insert_at_end(self, data):
        newnode = Node(data)
        p = self.head
        if self.head is None:
            self.head = newnode
        else:
            while p.next is not None:
                p = p.next
            newnode.prev = p
            p.next = newnode
    #INSERT AFTER A NODE
    def insert_after_node(self,data,x):
        temp = Node(data)
        p=self.head
        while p and p.data != x:
            p = p.next
        if p is None:
            print('Not found the number')
        if p is not None:
            temp.prev = p
            temp.next=p.next
            if p.next:
                p.next.prev=temp
            p.next = temp
    #INSERT BEFORE A NODE
    def insert_before_node(self,data,x):
        temp=Node(data)
        p=self.head
        while p.next is not None and p.next.data !=x:
            p=p.next
        if p is None:
            print("Not found the given number")
        if p is not None:
            temp.prev = p
            temp.next = p.next
            p.next.prev = temp
            p.next = temp
            
    def printList(self, node):
        print("\nTraversal in forward direction")
        while node:
            print("{}".format(node.data), end=" ")
            last = node
            node = node.next

        print("\nTraversal in reverse direction")
        while last:
            print("{}".format(last.data), end=" ")
            last = last.prev
    # def reverse(self,node):
    #     print("\nTraversal in reverse direction-----")
   
    #     while node:
    #         temp=node.prev
    #         node.prev = node.next 
    #         node.next = temp
    #         node = node.prev
    #     if temp:
    #         print(temp.next.data)
    #         print(temp.prev,temp.prev.data)
    #         self.head = temp.prev
    def remove(self,value):
        node = self.head
        if node is None:
            print("Linked list is empty")
        if self.head.data == value:
            node.next.prev = None
            self.head = node.next 
        else:
            while node.next is not None and node.next.data!=value:
                node = node.next
            print("\n",node.data)
            print(node.next.next.data)

            if node.next is None:
                print("Number not found in the linked list")
            elif node.next.next is not None:
                node.next=node.next.next
                node.next.prev=node
                
            elif node.next.next is None:
                node.next.prev = node
                node.next = None
  
arr=[i for i in range(1,6)]
dlist = Dlinkedlist()
for i in arr:
    dlist.insert_at_end(i)
# dlist.insert_at_start(10)
# dlist.insert_at_start(1)
# dlist.insert_at_start(0)
# dlist.insert_at_end(20)
dlist.insert_before_node(2,5)
dlist.printList(dlist.head)
print()
dlist.display()
print('\n')
dlist.display()
# dlist.reverse(dlist.head)
dlist.remove(2)
print()
dlist.display()
dlist.printList(dlist.head)