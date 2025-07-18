class TreeNode:
    def __init__(self,val=0,right=None,left=None):
        self.val = val
        self.left = left
        self.right = right
def postorderTraversal(root):
    if root:
        print(f'{root.val}-> ',end="")
        postorderTraversal(root.left)           
        postorderTraversal(root.right)

root = TreeNode('A')     
root.left = TreeNode('B')     
root.right = TreeNode('C')     
postorderTraversal(root)