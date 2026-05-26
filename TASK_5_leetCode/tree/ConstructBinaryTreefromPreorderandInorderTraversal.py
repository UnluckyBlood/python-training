# Построение бинарного дерева по обходу в прямом и обратном порядке
# Medium
# Темы
# Теги компании
# Подсказки
# Вам даны два целочисленных массива preorder и inorder.

# preorder — обход бинарного дерева в прямом порядке
# inorder — обход того же дерева в обратном порядке
# Оба массива имеют одинаковый размер и состоят из уникальных значений.
# Восстановите бинарное дерево по обходу в прямом и обратном порядке и верните его корень.

# Пример 1:



# Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

# Output: [1,2,3,null,null,null,4]
# Пример 2:

# Input: preorder = [1], inorder = [1]

# Output: [1]
# Ограничения:

# 1 <= inorder.length <= 1000.
# inorder.length == preorder.length
# -1000 <= preorder[i], inorder[i] <= 1000



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        root.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        
        return root