class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.val,end=" ")
            self.inorder(node.right)
    def preorder(self,node):
        if node:
            print(node.val,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val,end=" ")
    
tree = BinaryTree()

tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)
tree.root.right.left = TreeNode(6)
tree.root.right.right = TreeNode(7)

print(tree.inorder(tree.root))
print(tree.preorder(tree.root))
print(tree.postorder(tree.root))
    