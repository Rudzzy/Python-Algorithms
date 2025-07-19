class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def dfs_using_stack(root):
    if not root:
        return []
    
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
        
tree = TreeNode(1)
tree.left = TreeNode(2, TreeNode(4), TreeNode(5))
tree.right = TreeNode(3, None, TreeNode(6))

print(dfs_using_stack(tree))  

# Example:
#         1
#       /   \
#      2     3
#     / \     \
#    4   5     6
# Output: [1, 2, 4, 5, 3, 6]