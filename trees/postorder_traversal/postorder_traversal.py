class TreeNode:
    def __init__(self,val=0,right=None,left=None):
        self.val = val
        self.left = left
        self.right = right
def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)           
        postorderTraversal(root.right)
        print(f'{root.val}-> ',end="")

root = TreeNode('A')     
root.left = TreeNode('B')     
root.right = TreeNode('C')     
postorderTraversal(root)