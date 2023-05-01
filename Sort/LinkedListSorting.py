class Node:
    def __init__(self,data=None):
        self.data=data
        self.next = None
class LinkedList:
    def __init__(self,head=None):
        self.head = head
    def display(self):
        if self.head is None:
            print("Nothing")
        else:
            node = self.head
            while node is not None:
                print(node.data,end=" ")
                node = node.next 
    def insert(self,data):
        temp=Node(data)
        if self.head is None:
            self.head=temp
        else:
            node=self.head
            while node.next is not None:
                node = node.next
            node.next = temp
    def mergeSort(self,head):
        # if head is None or head.next is None:
        #     return head
        
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        
        first = head
        last = mid.next
        mid.next=None
        left = self.mergeSort(first)
        right= self.mergeSort(last)
        return self.join(left,right)
    def get_mid(self,head):
        if head is None: 
            return head
        slow = fast = head
        while fast.next and fast.next.next is not None:
            slow = slow.next 
            fast = fast.next.next 
        
        return slow
    def join(self,first,last):
        cur=dummy=Node()
        while first and last:
            if first.data<last.data:
                cur.next=first
                first=first.next 
            else:
                cur.next = last
                last = last.next 
            cur=cur.next
        cur.next = first or last
        return dummy.next

#Bubble Sort
    def bubbleSort(self):
        if self.head is None:
            print("Nothing")
        while True:
            node = self.head
            prev=None
            swapped = False
            while node.next is not None:
                if node.data > node.next.data:
                    temp = node.next
                    node.next = temp.next
                    temp.next=node
                    if prev is not None:
                        prev.next = temp
                    else:
                        self.head = temp
                    prev = temp
                    swapped = True
                else:
                    prev = node
                    node = node.next
            if not swapped:
                break
#Selection Sort
    def selectionSort(self):
        if self.head is None:
            print("Nothing")
        node = self.head
        
        while node and node.next:
            cur=node
            node1=node.next
            while node1:
                if node1.data<cur.data:
                    cur = node1
                node1 = node1.next
            self.display()
            print()
            if node.data>cur.data:
                node.data,cur.data=cur.data,node.data
            node = node.next
            
        print()
#Insertion Sort
    def insertionSort(self):
        if self.head is None:
            print('None')
            
        node = self.head
        while node and node.next:
            current=node.next
            j=node
            while j.data>current.data:
                j.next.data,j.data=j.data,j.next.data
                j=node.next
            j.data = current.data
            node = node.next
                
    def quickSort(self):
        start = self.head.data
        left=self.head.next.data
        node=self.head
        while node.next:
            node = node.next
        right=node.data
        
            







list = LinkedList()
arr=[2,5,1,6,7,4,3,67,10]

for i in arr:
    list.insert(i)
list.display()
print()
# sorted_list = list.mergeSort(list.head)
# LinkedList(sorted_list).display()
list.insertionSort()
list.display()
