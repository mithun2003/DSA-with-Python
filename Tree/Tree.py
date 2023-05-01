class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self, level=0):
        res = "  "*level + str(self.val)+"\n"
        for child in self.children:
            res += child.__str__(level+1)
        return res

    def find(self,val):
        if self.val == val:
            return val
        for child in self.children:
            node = child.find(val)
            if node:
                return node
        return None
def count_nodes(root):
    if not root:
        return 0
    count = 1
    for child in root.children:
        count += count_nodes(child)
    return count


def max_depth(root):
    if not root:
        return 0
    if not root.children:
        return 1
    maxDepth = 0
    for child in root.children:
        maxDepth = max(maxDepth, max_depth(child))
    return maxDepth+1


root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)
child4 = TreeNode(5)
child5 = TreeNode(6)
child6 = TreeNode(7)
child7 = TreeNode(8)
child8 = TreeNode(9)

root.children = [child1, child2, child3]
child1.add_child(child4)
child1.add_child(child5)
child2.add_child(child6)
child2.add_child(child7)
child2.add_child(child8)
child3.add_child(child8)
print(root)
print("No.of counts = ", count_nodes(root))
print("Max Depth = ", max_depth(root))
print(root.find(1))