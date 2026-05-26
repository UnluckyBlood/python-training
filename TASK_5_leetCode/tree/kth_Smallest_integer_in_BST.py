# K-е наименьшее целое число в двоичном дереве поиска
# Medium
# Темы
# Теги компании
# Подсказки
# Для root бинарного дерева поиска и целого числа k верните kth наименьшее значение (с индексом 1) в дереве.

# Бинарное дерево поиска удовлетворяет следующим ограничениям:

# Левое поддерево каждого узла содержит только узлы с ключами меньше ключа данного узла.
# Правое поддерево каждого узла содержит только узлы с ключами больше ключа данного узла.
# И левое, и правое поддеревья также являются деревьями двоичного поиска.
# Пример 1:



# Input: root = [2,1,3], k = 1

# Output: 1
# Пример 2:



# Input: root = [4,3,5,2,null], k = 4

# Output: 5
# Ограничения:

# 1 <= k <= The number of nodes in the tree <= 1000.
# 0 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        count = 0
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            count += 1
            if count == k:
                return current.val
            
            current = current.right
        
        return -1