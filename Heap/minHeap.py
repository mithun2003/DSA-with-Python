class Heap:
    def __init__(self):
        self.list = []

    def buildHeap(self, arr):
        self._buildHeap(arr)

    def _buildHeap(self, arr):
        self.list = arr
        for i in range(self.parent(len(self.list)-1), -1, -1):
            self.swiftDown(i)

    def swiftDown(self, currentNode):
        endIdx = len(self.list)-1
        leftIdx = self.leftChild(currentNode)
        while leftIdx <= endIdx:
            rightIdx = self.rightChild(currentNode)
            if rightIdx <= endIdx and self.list[rightIdx] < self.list[leftIdx]:
                idxSwift = rightIdx
            else:
                idxSwift = leftIdx

            if self.list[currentNode] > self.list[idxSwift]:
                self.list[currentNode], self.list[idxSwift] = self.list[idxSwift], self.list[currentNode]
            else:
                return

    def swiftUp(self, currentNode):
        parentIdx = self.parent(currentNode)
        while currentNode > 0 and self.list[parentIdx] > self.list[currentNode]:
            self.list[parentIdx], self.list[currentNode] = self.list[currentNode], self.list[parentIdx]
            currentNode = parentIdx
            parentIdx = self.parent(currentNode)

    def remove(self):
        self.list[0], self.list[-1] = self.list[-1], self.list[0]
        self.list.pop()

        self.swiftDown(0)

    def insert(self, value):
        self.list.append(value)
        self.swiftUp(len(self.list)-1)

    def parent(self, i):
        return (i-1)//2

    def leftChild(self, i):
        return (2*i+1)

    def rightChild(self, i):
        return (2*i+2)

    def display(self):
        print(self.list)
        for i in range(len(self.list)):
            print(self.list[i])

    def levelOrder(self):
        queue = [0]
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                idx = queue.pop(0)
                # print("idx",idx)
                print(self.list[idx], end=' ')
                left_child_idx = self.leftChild(idx)
                right_child_idx = self.rightChild(idx)
                if left_child_idx < len(self.list):
                    queue.append(left_child_idx)
                if right_child_idx < len(self.list):
                    queue.append(right_child_idx)
            print()


heap = Heap()
heap.buildHeap([32, 23])
heap.insert(-5)
heap.insert(5)
heap.insert(15)
heap.insert(25)
heap.insert(55)
heap.display()
# heap.remove()
print("mithun")
heap.display()
print("mithun")
heap.levelOrder()
