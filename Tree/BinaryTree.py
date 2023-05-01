class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinaryTreeNode:
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if node.left is None:
            node.left = Node(val)
        elif node.right is None:
            node.right = Node(val)
        else:
            if self.count(node.left) <= self.count(node.right):
                self._insert(node.left, val)
            else:
                self._insert(node.right, val)

    def inOrder(self):
        self._inOrder(self.root)

    def _inOrder(self, node):
        if node is not None:
            self._inOrder(node.left)
            print(node.data)
            self._inOrder(node.right)

    def count(self, node):
        if node is None:
            return 0
        return 1+self.count(node.left)+self.count(node.right)

    def print_tree(self):
        if not self:
            return

        current_level = [(self.root)]
        while current_level:
            next_level = []
            output = ""
            for node in current_level:
                output += str(node.data) + " "
                if node.left:
                    next_level.append((node.left))
                if node.right:
                    next_level.append((node.right))
            print("Level", ":", output)
            current_level = next_level
    def isBST(self):
        vals=[]
        def check(root):
            if root is not None:
                check(root.left)
                vals.append(root.data)
                check(root.right)
        check(self.root)
        for i in range(1,len(vals)):
            if vals[i]<=vals[i-1]:
                return False
        return True

root = BinaryTreeNode()
elements = [55,44,66]
for element in elements:
    root.insert(element)
print(root.inOrder())
root.print_tree()
print()
print(root.isBST())
