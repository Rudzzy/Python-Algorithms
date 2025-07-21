class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return (is_valid_bst(root.left, low, root.val) and
            is_valid_bst(root.right, root.val, high))

tree = TreeNode(5)
tree.left = TreeNode(3, TreeNode(2), TreeNode(4))
tree.right = TreeNode(7, TreeNode(6), TreeNode(8))

result = is_valid_bst(tree)

if result:
    print("This is a valid BST")
else:
    print("This is NOT a valid BST")