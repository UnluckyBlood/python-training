# Допустимое Двоичное Дерево Поиска
# Medium
# Темы
# Теги компании
# Подсказки
# Для root бинарного дерева верните true, если оно является корректным бинарным деревом поиска, в противном случае верните false.

# корректное бинарное дерево поиска удовлетворяет следующим ограничениям:

# Левое поддерево каждого узла содержит только узлы с ключами меньше ключа данного узла.
# Правое поддерево каждого узла содержит только узлы с ключами больше ключа данного узла.
# И левое, и правое поддеревья также являются деревьями двоичного поиска.
# Пример 1:



# Input: root = [2,1,3]

# Output: true
# Пример 2:



# Input: root = [1,2,3]

# Output: false
# Пояснение: значение корневого узла равно 1, но значение его левого потомка равно 2, что больше 1.

# Ограничения:

# 1 <= The number of nodes in the tree <= 1000.
# -1000 <= Node.val <= 1000

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float('inf'))

