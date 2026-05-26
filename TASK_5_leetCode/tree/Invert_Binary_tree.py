# Инвертировать Двоичное дерево
# Легко
# Темы
# Теги компании
# Подсказки
# Вам дан корень бинарного дерева root. Поверните бинарное дерево и верните его корень.

# Пример 1:



# Input: root = [1,2,3,4,5,6,7]

# Output: [1,3,2,7,6,5,4]
# Пример 2:



# Input: root = [3,2,1]

# Output: [3,1,2]
# Пример 3:

# Input: root = []

# Output: []
# Ограничения:

# 0 <= The number of nodes in the tree <= 100.
# -100 <= Node.val <= 100


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        root.left = right_inverted
        root.right = left_inverted
        return root