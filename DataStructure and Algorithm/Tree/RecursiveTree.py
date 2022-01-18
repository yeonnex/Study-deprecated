class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

def recursivePreOrder(node):
    if node is None:
        return
    print(node.val, end= ' ')
    recursivePreOrder(node.left)
    recursivePreOrder(node.right)

def recursiveInOrder(node):
    if node is None:
        return
    recursiveInOrder(node.left)
    print(node.val, end=" ")
    recursiveInOrder(node.right)

def recursivePostOrder(node):
    if node is None:
        return
    recursivePostOrder(node.left)
    recursivePostOrder(node.right)
    print(node.val, end=" ")

recursivePreOrder(node1)
print()
recursiveInOrder(node1)
print()
recursivePostOrder(node1)


