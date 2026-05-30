# 94. Обход бинарного дерева в прямом порядке
# Решено
# Легко
# Темы
# значок премиум-замка
# Компании
# Для root бинарного дерева верните последовательность обхода его узлов в прямом порядке.

 

# Пример 1:

# Входные данные: root = [1,null,2,3]

# Выходные данные: [1,3,2]

# Пояснение:



# Пример 2:

# Входные данные: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Выходные данные: [4,2,6,5,7,1,3,9,8]

# Пояснение:



# Пример 3:

# Входные данные: root = []

# Выходные данные: []

# Пример 4:

# Входные данные: root = [1]

# Выходные данные: [1]

 

# Ограничения:

# Количество узлов в дереве находится в диапазоне [0, 100].
# -100 <= Node.val <= 100
 

# Продолжение: Рекурсивное решение тривиально, а можно ли сделать это итеративно?


from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result