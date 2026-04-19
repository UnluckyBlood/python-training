# Удаление узла из конца связанного списка
# Medium
# Темы
# Теги компании
# Подсказки
# Вам дан начальный узел связного списка head и целое число n.

# Удалите узел nth из конца списка и верните начальный узел списка.

# Пример 1:

# Input: head = [1,2,3,4], n = 2

# Output: [1,2,4]
# Пример 2:

# Input: head = [5], n = 1

# Output: []
# Пример 3:

# Input: head = [1,2], n = 2

# Output: [2]
# Ограничения:

# Количество узлов в списке равно sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next
    
    
