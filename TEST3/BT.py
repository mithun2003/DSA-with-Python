class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        node = self.root
        if node is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if node.left is None:
            node.left = Node(data)
        elif node.right is None:
            node.right = Node(data)
        else:
            if self.count(node.left) <= self.count(node.right):
                self._insert(node.left,data)
            else:
                self._insert(node.right,data)
                
    def count(self,node):
        if node is None:
            return 0
        return 1+self.count(node.left)+self.count(node.right)
                
    def levelOrder(self):
        if not self:
            return None
        
        current = [self.root]
        while current:
            next = []
            output =""
            for node in current:
                output+=str(node.data)+" "
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            print(output)
            current = next
                    
                    
bt = BinaryTree()
ele=[2,43,6,3,45,56,4,33]
for i in ele:
    bt.insert(i)
    
bt.levelOrder()