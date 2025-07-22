from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def search_bfs(root, target):
    if not root:
        return False
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node.val == target:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False


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
print(search_bfs(tree, target))  # Output: True