# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.left = None
#         self.right = None


# class BinaryST:
#     def __init__(self, root=None):
#         self.root = root

#     def insert(self, value):
#         node = self.root
#         if node is None:
#             self.root = Node(value)
#             return
#         else:
#             while True:
#                 if value <= node.data:
#                     if node.left is None:
#                         node.left = Node(value)
#                         break
#                     else:
#                         node = node.left
#                 else:
#                     if node.right is None:
#                         node.right = Node(value)
#                         break
#                     else:
#                         node = node.right

#     def search(self, data):
#         node = self.root
#         while node is not None:
#             if data < node.data:
#                 node = node.left
#             elif data > node.data:
#                 node = node.right
#             else:
#                 return True
#         return False

#     def minVal(self, node):
#         if node.left is None:
#             return node.data
#         else:
#             return self.minVal(node.left)

#     def remove(self,data):
#         self.removeHelper(data,self.root,None)
#     def removeHelper(self,data,currentNode,parentNode):
#         while currentNode is not None:
#             if data>currentNode.data:
#                 parentNode = currentNode
#                 currentNode = currentNode.left
#             elif data<currentNode.data:
#                 parentNode = currentNode
#                 currentNode = currentNode.right
#             else:
#                 if currentNode.left is not None and currentNode.right is not None:
#                     currentNode.data = self.minVal(currentNode.right)
#                     self.remove(currentNode.data,currentNode.right,currentNode)
#                 else:
#                     if parentNode is None:
#                         if currentNode.right is None:
#                             self.root = currentNode.left
#                         else:
#                             self.root = currentNode.right
#                     else:
#                         if parentNode.left == currentNode:
#                             if currentNode.right is None:
#                                 parentNode.left = currentNode.left
#                             else:
#                                 parentNode.left = currentNode.right
#                         else:
#                             if currentNode.right is None:
#                                 parentNode.right = currentNode.left
#                             else:
#                                 parentNode.right = currentNode.right
#                     break

#     def inOrder(self):
#         self._inOrder(self.root)

#     def _inOrder(self, node):
#         if node is not None:
#             self._inOrder(node.left)
#             print(node.data)
#             self._inOrder(node.right)

#     def levelOrder(self):
#         if self.root is None:
#             return
#         current = [self.root]
#         while current:
#             next = []
#             output = ""
#             for node in current:
#                 output += str(node.data)+" "
#                 if node.left:
#                     next.append(node.left)
#                 if node.right:
#                     next.append(node.right)
#             print(output)
#             current = next


# bst = BinaryST()
# bst.insert(6)
# bst.insert(3)
# bst.insert(9)
# bst.insert(98)
# bst.insert(-9)

# bst.inOrder()
# print("nd")
# bst.levelOrder()


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinaryST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        node = self.root
        if node is None:
            self.root = Node(data)
            return
        else:
            while True:
                if data <= node.data:
                    if node.left is None:
                        node.left = Node(data)
                        break
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = Node(data)
                        break
                    else:
                        node = node.right

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
    def remove(self,val):
        self.removeHelper(val,self.root,None)
    
    def removeHelper(self,data,currentNode,parentNode):
        while currentNode is not None:
            if data<=currentNode.data:
                parentNode=currentNode
                currentNode=currentNode.left
            elif data> currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.data = self.minVal(currentNode.right)
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
                            
                    
                    
    def minVal(self,node):
        if node.left is None:
            return node.data
        else:
            return self.minVal(node.left)
    
    def inOrder(self):
        vals = []

        def _inOrder(node):
            if node is not None:
                _inOrder(node.left)
                vals.append(node.data)
                _inOrder(node.right)
        _inOrder(self.root)
        print(vals)

    def levelOrder(self):
        if self.root is None:
            return
        current = [self.root]
        while current:
            next = []
            output = ""
            for node in current:
                output += str(node.data)+" "
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            print(output)
            current = next


bst = BinaryST()
bst.insert(6)
bst.insert(3)
bst.insert(9)
bst.insert(98)
bst.insert(-9)
print(bst.Search(9))

bst.inOrder()
bst.levelOrder()
