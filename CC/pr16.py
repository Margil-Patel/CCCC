class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def mirror(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        
        return (root1.val==root2.val) and self.mirror(root1.left,root2.right) and self.mirror(root1.right,root2.left)
    
tree1 = BinaryTree()
tree2 = BinaryTree()

tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)
tree1.root.right.left = Node(6)
tree1.root.right.right = Node(7)

tree2.root = Node(1)
tree2.root.left = Node(3)
tree2.root.right = Node(2)
tree2.root.left.left = Node(7)
tree2.root.left.right = Node(6)
tree2.root.right.left = Node(5)
tree2.root.right.right = Node(4)

if tree1.mirror(tree1.root,tree2.root):
    print("Mirror")
else:
    print("NO")

