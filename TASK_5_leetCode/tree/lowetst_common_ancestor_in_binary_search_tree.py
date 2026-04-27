# Наименьший общий предок в бинарном дереве поиска
# Medium
# Темы
# Теги компании
# Подсказки
# Для бинарного дерева поиска (BST), в котором все значения узлов уникальны, и двух узлов дерева p и q найдите наименьшего общего предка (НОП) этих двух узлов.

# Самый низкий общий предок двух узлов p и q — это самый нижний узел в дереве T, у которого p и q являются потомками. Предк может быть потомком самого себя.

# Пример 1:



# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

# Output: 5
# Пример 2:



# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

# Output: 3
# Пояснение: LCA узлов 3 и 4 равен 3, поскольку узел может быть потомком самого себя.

# Ограничения:

# 2 <= The number of nodes in the tree <= 100.
# -100 <= Node.val <= 100
# p != q
# p и q будут существовать в двоичном дереве поиска.







# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current