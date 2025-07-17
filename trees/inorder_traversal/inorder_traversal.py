class TreeNode:
    def __init__(self,val=0,right=None,left=None):
        self.val = val
        self.left = left
        self.right = right
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)           
        print(f'{root.val}-> ',end="")
        inorderTraversal(root.right)

root = TreeNode('A')     
root.left = TreeNode('B')     
root.right = TreeNode('C')     
inorderTraversal(root)