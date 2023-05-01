class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, value):
        temp = Node(value)
        node = self.head
        if node is None:
            # temp.next = self.head
            self.head = temp
        else:
            while node.next is not None:
                node = node.next
            node.next = temp

    def display(self):
        p = self.head
        if p is None:
            print("THE LIST IS EMPTY")
        while p is not None:
            print(p.data, end=" ")
            p = p.next
        print()

    def add_values(self):
        num = int(
            input("Enter how many number you want to add in the Linked List : "))
        arr = []
        for i in range(0, num):
            values = int(input("ENTER THE "+str(i+1)+" VALUE : "))
            arr.append(values)
        for i in arr:
            list.add(i)

    def remove_duplicates(self):
        node = self.head
        seen = set()
        duplicates = set()
        prev = None
        while node is not None:
            if node.data in seen:
                duplicates.add(node.data)
            else:
                seen.add(node.data)
            node = node.next
        node = self.head
        while node is not None:
            if node.data in duplicates:
                if prev is not None:
                    prev.next = node.next
                else:
                    self.head = node.next
            else:
                prev = node
            node = node.next

    def middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data


list = LinkedList()
list.add_values()
list.display()
# print(list.middle())
list.removetwo()
# list.remove_duplicates()
list.display()


# def remove(self):
#     node = self.head
#     seen=set()
#     duplicate=set()
#     prev=None
#     while node is not None:
#         if node.data in seen:
#             duplicate.add(node.data)
#         else:
#             seen.add(node.data)
#         node = node.next
#     node = self.head
#     while node is not None:
#         if node.data in duplicate:
#             if prev is not None:
#                 prev.next =node.next
#             else:
#                 self.head = node.next
#         else:
#             prev = node
#         node = node.next
