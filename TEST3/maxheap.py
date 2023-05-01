class Heap:
    def __init__(self):
        self.heap = []

    def buildHeap(self, arr):
        self.heap = arr
        self._buildHeap()

    def _buildHeap(self):
        for i in range(self.parent(len(self.heap)-1), -1, -1):
            self.swiftDown(i)

    def swiftDown(self, current):
        end = len(self.heap)-1
        left = self.lChild(current)
        while left <= end:
            right = self.rChild(current)
            if right <= end and self.heap[left] < self.heap[right]:
                toSwift = right
            else:
                toSwift = left
            if self.heap[current] < self.heap[toSwift]:
                self.heap[current], self.heap[toSwift] = self.heap[toSwift], self.heap[current]
            else:
                return
            current = toSwift
            left = self.lChild(current)
            
    def swiftUp(self,current):
        parent = self.parent(current)
        while current>0 and self.heap[parent]<self.heap[current]:
            self.heap[parent],self.heap[current] = self.heap[current],self.heap[parent]
            current = parent
            parent = self.parent(current)
            
    def insert(self,data):
        self.heap.append(data)
        self.swiftUp(len(self.heap)-1)
        
    def remove(self):
        self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
        self.heap.pop()
        self.swiftDown(0)

    def heapSort(self):
        for i in range(len(self.heap)-1,0,-1):
            self.heap[i],self.heap[0]=self.heap[0],self.heap[i]
            self.swiftDownRange(0,i-1)
    def swiftDownRange(self,start,end):
        root = start
        while self.lChild(root)<=end:
            left = self.lChild(root)
            swap = root
            if self.heap[swap]<self.heap[left]:
                swap = left
            if left+1<=end and self.heap[swap]<self.heap[left+1]:
                swap = left+1
            if swap == root:
                return 
            else:
                self.heap[swap],self.heap[root]=self.heap[root],self.heap[swap]
                root = swap 
    
    def display(self):
        for i in self.heap:
            print(i)

    def parent(self, i):
        return (i-1)//2

    def lChild(self, i):
        return (2*i)+1

    def rChild(self, i):
        return (2*i)+2


h = Heap()
h.buildHeap([2, 4, 5])
h.insert(6)
h.insert(1)
h.insert(9)
h.insert(8)
h.display()
h.remove()
print("hds")
h.display()
h.heapSort()
print()
h.display()
