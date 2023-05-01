class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        else:
            node = self.root
            while True:
                if data <= node.data:
                    if node.left is None:
                        node.left = Node(data)
                        break
                    else:
                        node = node.left
                elif data > node.data:
                    if node.right is None:
                        node.right = Node(data)
                        break
                    else:
                        node = node.right
    def closest_value(self,target):
        node = self.root
        closest = float("inf")
        while node is not None:
            if abs(node.data-target)<abs(closest-target):
                closest = node.data
            if target < node.data:
                node = node.left
            elif target > node.data:
                node = node.right
            else:
                return node.data
        return closest
    def Search(self, val):
        node = self.root
        while node is not None:
            if val < node.data:
                node = node.left
            elif val > node.data:
                node = node.right
            else:
                return True
        return False
        
    def levelOrder(self):
        if self.root is None:
            return
        current = [self.root]
        while current:
            next =[]
            output=""
            for node in current:
                output+=str(node.data)+" "
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            print(output)
            current = next
    def remove(self,val):
        self._remove(val,self.root,None)
        
    def _remove(self,val,currentNode,parentNode):
        while currentNode is not None:
            if val<currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.left
            elif val>currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.data = self.minVal(currentNode.right)
                    self._remove(currentNode.data,currentNode.right,currentNode)
                else:
                    if parentNode is None:
                        if currentNode.right is None:
                            self.root=currentNode.left
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
                        
    def minVal(self,node):
        if node.left is None:
            return node.data
        return self.minVal(node.left)

bst = BST()
ele = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
for i in ele:
    bst.insert(i)
bst.levelOrder()
print(bst.Search(15))
bst.remove(50)
print(bst.Search(15))
bst.levelOrder()
print(bst.closest_value(4))
