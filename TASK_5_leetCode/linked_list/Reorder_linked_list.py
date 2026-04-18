# Измените Порядок Связанного списка
# Medium
# Темы
# Теги компании
# Подсказки
# Вам дана голова односвязного списка.

# Позиции в связанном списке из length = 7 элементов, например, могут изначально выглядеть так:

# [0, 1, 2, 3, 4, 5, 6]

# Переставьте узлы связанного списка в следующем порядке:

# [0, 6, 1, 5, 2, 4, 3]

# Обратите внимание, что в общем случае для списка из length = n элементов узлы переставляются в следующем порядке:

# [0, n-1, 1, n-2, 2, n-3, ...]

# Вы не можете изменять значения в узлах списка, вместо этого вам нужно переставить сами узлы.

# Пример 1:

# Input: head = [2,4,6,8]

# Output: [2,8,4,6]
# Пример 2:

# Input: head = [2,4,6,8,10]

# Output: [2,10,4,8,6]
# Ограничения:

# 1 <= Length of the list <= 1000.
# 1 <= Node.val <= 1000





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2