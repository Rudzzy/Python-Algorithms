class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def dfs_using_recursion(root):
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
        
    dfs(root)
    return result

        
tree = TreeNode(1)
tree.left = TreeNode(2, TreeNode(4), TreeNode(5))
tree.right = TreeNode(3, None, TreeNode(6))

print(dfs_using_recursion(tree))  

# Example:
#         1
#       /   \
#      2     3
#     / \     \
#    4   5     6
# Output: [1, 2, 4, 5, 3, 6]