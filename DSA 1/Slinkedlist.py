class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    # FOR DISPLAY ELEMENTS

    def display(self):
        p = self.head
        if p is None:
            print("---No elements in the linked list---")
        while p is not None:
            print(p.data, end=" ")
            p = p.next
            
    # INSERT A VALUE AT THE END

    def insert_at_end(self, newdata):
        temp = Node(newdata)
        if self.head == None:
            self.head = temp
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = temp

    # INSERT A VALUE AT THE START

    def insert_at_beginning(self, newdata):
        temp = Node(newdata)
        temp.next = self.head
        self.head = temp

    # INSERT A VALUE AFTER A NODE

    def insert_after_node(self, data, x):
        temp = Node(data)
        p = self.head
        print(p.data)
        while p is not None:
            if p.data == x:
                break
            p = p.next
        print("P>DATA", p.data)
        if p is None:
            print(x, "not found in the list")
        else:
            temp.next = p.next
            p.next = temp

    # INSERT A VALUE BEFORE A NODE

    def insert_before_node(self, data, x):
        if self.head is None:
            print("The list is empty")
        newnode = Node(data)
        p = self.head
        if x == p.data:
            newnode.next = self.head
            self.head = newnode
        while p.next is not None:
            if x == p.next.data:
                break
            p = p.next
        if p.next is None:
            print(x, "not found in the list")
        else:
            newnode.next = p.next
            p.next = newnode

    # REVERSE LIST USING NEXT AND PREV

    def reverse(self):
        pre = None
        p = self.head
        while p is not None:
            next = p.next
            p.next = pre
            pre = p
            p = next
        self.head = pre

    # CONVERT ARRAY TO LINKED LIST

    def array_to_list(self, arr):
        if not arr:
            return None
        for i in range(0, len(arr)):
            self.insert_at_end(arr[i])

    # REVERSE THE LIST IN RECURSIVE METHOD

    def reverseList(self, node):
        if node is None:
            return
        self.reverseList(node.next)
        print(node.data, end=" ")

    # REMOVE DUPLICATE ELEMENT FROM THE LIST

    def duplicateremove(self, node):
        if node is None:
            return
        while node is not None and node.next is not None:
            if node.data == node.next.data:
                node.next = node.next.next
            node = node.next
    def duplicate(self):
        head = self.head
        if head is None:
            return -1
        s = set()
        node = head.next
        prev=head 
        while head.next is not None:
            p = head
            while p.next is not None:
                if head.data == p.next.data:
                    s.add(head.data)
                    print(head.data)
                    print(p.data)
                    
                    # self.head = self.head.next
                    # if p.next.next ==None:
                    #     p.next = None
                    # else:
                    #     p.next=p.next.next
                    
                    # print(p)
                    # if p.next is None:
                    #     p=None
                    # else:
                    #     p=p.next
                # else:
                    # s.add(head.data)
                p=p.next
            head = head.next
        print(s)
        
    # REMOVE A SPECIFIC VALUE FROM THE LIST

    def remove(self, value):
        node = self.head
        if node is None:
            print("Linked list is empty")
        if self.head.data == value:
            self.head = node.next
        else:
            while node is not None and node.next is not None:
                if node.next.data == value:
                    print(node.next.data, node.data)
                    break
                node = node.next
            if node.next is None:
                print("Number not found in the linked list")
            elif node.next.next is not None:
                node.next = node.next.next
            elif node.next.next is None:
                print('---', node.data)
                node.next = None

        # print("Number not found in the linked list")
    def deletAll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = None

    def search(self, num):
        p = self.head
        i = 1
        if p is None:
            print("Linked list is empty")
        while p.next is not None and p.data != num:
            i += 1
            p = p.next
        if p.data == num:
            print("Number found at "+str(i))
    def removetwo(self,head):
        if not head:
            return
        print(head.data)
        if head.next:
            self.removetwo(head.next.next)

list = SLinkedList()
# list.insert_at_beginning(40)
# list.insert_at_end(50)
# list.insert_after_node(10,40)
# list.insert_before_node(5,50)
list.array_to_list([1,2,3,4,5])
# list.array_to_list([60,70,80,90,70,60,30,60])
list.display()
print()
list.removetwo(list.head)
list.display()
