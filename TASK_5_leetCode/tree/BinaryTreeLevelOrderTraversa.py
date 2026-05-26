# Binary Tree Level Order Traversal
# Medium
# Topics
# Company Tags
# Hints
# Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

# Example 1:



# Input: root = [1,2,3,4,5,6,7]

# Output: [[1],[2,3],[4,5,6,7]]
# Example 2:

# Input: root = [1]

# Output: [[1]]
# Example 3:

# Input: root = []

# Output: []
# Constraints:

# 0 <= The number of nodes in the tree <= 1000.
# -1000 <= Node.val <= 1000


# Topics


from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        current_level = [root]  # список узлов текущего уровня
        
        while current_level:
            # Собираем значения текущего уровня
            level_values = [node.val for node in current_level]
            result.append(level_values)
            
            # Формируем следующий уровень
            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            current_level = next_level  # переходим на следующий уровень
        
        return result