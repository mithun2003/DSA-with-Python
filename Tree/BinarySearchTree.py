class BinaryNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        node = self.root
        if node is None:
            self.root = BinaryNode(data)
            return
        else:
            # node = self.root
            while True:
                # print(node.data)
                if data <= node.data:
                    if node.left is None:
                        node.left = BinaryNode(data)
                        break
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = BinaryNode(data)
                        break
                    else:
                        node = node.right

    def search(self, data):
        node = self.root
        while node is not None:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                return True
        return False

    def remove(self, data):
        self.removeHelper(data,self.root,None)
    def removeHelper(self,data,currentNode,parentNode):
        while currentNode is not None:
            if data<currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.left
            elif data>currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    #for find the min value from right side of the tree
                    currentNode.data = self.getMinVal(currentNode.right)
                    self.removeHelper(currentNode.data,currentNode.right,currentNode)
                else:
                    if parentNode is None:
                        if currentNode.right is None:
                            self.root = currentNode.left
                        else:
                            self.root = currentNode.right
                    else:
                        if parentNode.left == currentNode:
                            if currentNode.right is None:
                                parentNode.left = currentNode.left
                            else:
                                parentNode.left = currentNode.right
                        else:
                            if currentNode.right is None:
                                parentNode.right = currentNode.left
                            else:
                                parentNode.right = currentNode.right
                    break
                 
    def getMinVal(self, node):
        print("Node", node.data)
        if node.left is None:
            return node.data
        else:
            return self.getMinVal(node.left)

    def getMaxVal(self, node):
        if node.right is None:
            return node.data
        else:
            return self.getMaxVal(node.right)

    def levelOrder(self):
        if self.root is None:
            return
        currentNode = [self.root]
        while currentNode:
            next = []
            output = ""
            for node in currentNode:
                output += str(node.data)+" "
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            print(output)
            currentNode = next
            

    def inOrder(self):
        self._inOrder(self.root)

    def _inOrder(self, node):
        if node is not None:
            self._inOrder(node.left)
            print(node.data, end=" ")
            self._inOrder(node.right)


root = BinaryTree()
root.insert(15)
root.insert(10)
root.insert(11)
root.insert(20)
root.insert(3)
root.insert(17)
root.inOrder()
print()
print(root.search(17))
root.levelOrder()
print(root.getMinVal(root.root))
print(root.getMaxVal(root.root))

root.remove(15)
print("\n\n")
root.levelOrder()