class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev=None
class DlinkedList:
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail = tail
    def display(self):
        node = self.head
        if node is None:
            print("Linked list is empty")
        else:
            while node:
                print(node.data,end=" ")
                node = node.next 
    
    def insertvalue(self,data):
        temp = Node(data)
        node = self.head
        
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            while node.next is not None:
                node=node.next
            temp.prev=node
            node.next = temp
            self.tail = temp
    
    def innersum(self):
        list=[]
        head = self.head
        tail = self.tail
        while head != tail:
            val = head.data+tail.data
            list.append(val)
            head = head.next
            tail = tail.prev
            if head == tail.next:
                break
        if head == tail : 
            list.append(tail.data)
        print(list)
            
        
list = DlinkedList()
arr=[i for i in range(1,10)]
# arr=[45,1,2,6,9,7,5,5]
for i in range(len(arr)):
    list.insertvalue(arr[i])
list.display()
print()
list.innersum()
list.display()