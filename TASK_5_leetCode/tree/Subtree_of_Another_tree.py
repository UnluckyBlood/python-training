# Поддерево Другого дерева
# Легко
# Темы
# Теги компании
# Подсказки
# Для заданных корней двух бинарных деревьев root и subRoot верните true в случае, если существует поддерево root с той же структурой и значениями узлов subRoot, и false в противном случае.

# Поддерево бинарного дерева tree — это дерево, состоящее из узла tree и всех его потомков. Дерево tree также можно считать поддеревом самого себя.

# Пример 1:



# Input: root = [1,2,3,4,5], subRoot = [2,4,5]

# Output: true
# Пример 2:



# Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

# Output: false
# Ограничения:

# 1 <= The number of nodes in both trees <= 100.
# -100 <= root.val, subRoot.val <= 100



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right 
        self.left = left

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) ->bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode) ->bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
    

