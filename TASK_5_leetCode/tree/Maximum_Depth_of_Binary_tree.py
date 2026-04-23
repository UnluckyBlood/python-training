# Максимальная глубина бинарного дерева
# Легко
# Темы
# Теги компании
# Подсказки
# Для заданного root бинарного дерева верните его глубину.

# Глубина бинарного дерева определяется как количество узлов на самом длинном пути от корневого узла до самого дальнего листового узла.

# Пример 1:



# Input: root = [1,2,3,null,null,4]

# Output: 3
# Пример 2:

# Input: root = []

# Output: 0
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1+max(left_depth, right_depth)
    
# если пустой список мы сразу выводим 0, а если есть что-то мы выводим 1 + максимальная глубина какой-нибудь из сторон дерева
