class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, head=None):
        self.front = head
        self.rear = None

    def display(self):
        node = self.front
        if node is None:
            print("EMPTY")
        else:
            while node is not None:
                print(node.data, end=" ")
                node = node.next

    def enqueue(self, data):
        temp = Node(data)
        if self.rear is None:
            self.front = self.rear = temp
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.front is None:
            print("NO ELEMENTS")
            return
        self.front = self.front.next
        if self.front is None:
            self.rear = None


queue = Queue()

arr = [1, 2, 3, 4, 5]
for i in arr:
    queue.enqueue(i)
queue.display()
queue.dequeue()
queue.dequeue()
queue.dequeue()

print()
queue.display()
