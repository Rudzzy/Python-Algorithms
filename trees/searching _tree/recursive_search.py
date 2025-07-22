class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search_recursive(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    return search_recursive(root.left, target) or search_recursive(root.right, target)


# Example tree:
#         5
#       /   \
#      3     7
#     / \   / \
#    2  4  6   8

tree = TreeNode(5)
tree.left = TreeNode(3, TreeNode(2), TreeNode(4))
tree.right = TreeNode(7, TreeNode(6), TreeNode(8))

target = 6
print(search_recursive(tree, target))  # Output: True
