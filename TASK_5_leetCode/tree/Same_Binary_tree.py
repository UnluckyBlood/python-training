# Одно и то же Бинарное дерево
# Легко
# Темы
# Теги компании
# Подсказки
# Для заданных корней двух бинарных деревьев p и q верните true в случае, если деревья эквивалентны, в противном случае верните false.

# Два бинарных дерева считаются эквивалентными, если они имеют одинаковую структуру, а их узлы содержат одинаковые значения.

# Пример 1:



# Input: p = [1,2,3], q = [1,2,3]

# Output: true
# Пример 2:



# Input: p = [4,7], q = [4,null,7]

# Output: false
# Пример 3:



# Input: p = [1,2,3], q = [1,3,2]

# Output: false
# Ограничения:

# 0 <= The number of nodes in both trees <= 100.
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
