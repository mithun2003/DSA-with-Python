class MaxHeap:
    def __init__(self):
        self.heap = []

    def buildHeap(self, arr):
        self._buildHeap(arr)

    def _buildHeap(self, arr):
        self.heap = arr
        for i in range(self.parent(len(self.heap)-1), -1, -1):
            self.swiftDown(i)

    def swiftDown(self, currentNode):
        endIdx = len(self.heap)-1
        leftIdx = self.leftChild(currentNode)
        while leftIdx <= endIdx:
            rightIdx = self.rightChild(currentNode)
            if rightIdx <= endIdx and self.heap[rightIdx] > self.heap[leftIdx]:
                toSwiftIdx = rightIdx
            else:
                toSwiftIdx = leftIdx
            if self.heap[currentNode] < self.heap[toSwiftIdx]:
                self.heap[currentNode], self.heap[toSwiftIdx] = self.heap[toSwiftIdx], self.heap[currentNode]
            else:
                return
            currentNode = toSwiftIdx
            leftIdx = self.leftChild(currentNode)
    def swiftUp(self,currentNode):
        parentIdx = self.parent(currentNode)
        while currentNode > 0 and self.heap[currentNode]>self.heap[parentIdx]:
            self.heap[currentNode], self.heap[parentIdx] = self.heap[parentIdx], self.heap[currentNode]
            currentNode = parentIdx
            parentIdx = self.parent(currentNode)
            
    def insert(self,value):
        self.heap.append(value)
        self.swiftUp(len(self.heap)-1)

    def remove(self):
        self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
        self.heap.pop()
        self.swiftDown(0)
        
    def parent(self, i):
        return (i-1)//2

    def leftChild(self, i):
        return (2*i+1)

    def rightChild(self, i):
        return (2*i+2)
    def display(self):
        for i in self.heap:
            print(i)

    def levelOrder(self):
        queue = [0]
        while queue:
            size = len(queue)
            for i in range(size):
                idx = queue.pop(0)
                print(self.heap[idx],end=" ")
                leftIdx = self.leftChild(idx)
                rightIdx = self.rightChild(idx)
                if leftIdx<len(self.heap):
                    queue.append(leftIdx)
                if rightIdx<len(self.heap):
                    queue.append(rightIdx)
        print()
        
h = MaxHeap()
h.buildHeap([2,4,5])
h.insert(6)
h.insert(1)
h.insert(9)
h.insert(8)

h.levelOrder()
h.display()
h.remove()
print("hds")
h.display()
h.levelOrder()