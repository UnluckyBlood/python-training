# Объединение K отсортированных связанных списков
# Сложные
# Темы
# Теги компании
# Подсказки
# Вам дан массив k связанных списков lists, каждый из которых отсортирован по возрастанию.

# Верните отсортированный связанный список, полученный в результате объединения всех отдельных связанных списков.

# Пример 1:

# Input: lists = [[1,2,4],[1,3,5],[3,6]]

# Output: [1,1,2,3,3,4,5,6]
# Пример 2:

# Input: lists = []

# Output: []
# Пример 3:

# Input: lists = [[]]

# Output: []
# Ограничения:

# 0 <= lists.length <= 1000
# 0 <= lists[i].length <= 100
# -1000 <= lists[i][j] <= 1000



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(mergeTwoLists(l1, l2))
            lists = merged

        return lists[0]
    


# в начале проверка есть ои список,
# следующая функция идёт базовое слияние двух сылочных списков, по возрастанию значения
# а след циклом мы по парно сливаем списки пока они не кончаться вызывая прошлую функцию
