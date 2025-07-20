from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs_using_queue(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

tree = TreeNode(1)
tree.left = TreeNode(2, TreeNode(4), TreeNode(5))
tree.right = TreeNode(3, None, TreeNode(6))

print(bfs_using_queue(tree))

# Example:
#         1
#       /   \
#      2     3
#     / \     \
#    4   5     6
# Output: [1, 2, 3, 4, 5, 6]