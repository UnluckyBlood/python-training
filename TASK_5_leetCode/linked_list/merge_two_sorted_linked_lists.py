# Merge Two Sorted Linked Lists
# Easy
# Topics
# Company Tags
# Hints
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:



# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]
# Example 2:

# Input: list1 = [], list2 = [1,2]

# Output: [1,2]
# Example 3:

# Input: list1 = [], list2 = []

# Output: []
# Constraints:

# 0 <= The length of the each list <= 100.
# -100 <= Node.val <= 100


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        new_list = dummy
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next
        if list1 is not None:
            new_list.next = list1
        if list2 is not None:
            new_list.next = list2
        return dummy.next
    
# по сути мы создаём список проверку мы может делать только and, а не or так как если один из них станет None, выдаст ошибку при сравнении, поэтому в конце мы делаем доп проверку и запись, если вдруг осталось число
# .next обращение к следующему элементу, так что все действия мы можем делать обращаясь так 

# чтобы было быстрее при больших числах используют в начале проверку на пустоту списков, чтобы если что вернуть не пустой 
        # if not list1:
        #     return list2
        
        # if not list2:
        #     return list1




        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        top = res
        if not list1:
            return list2
        
        if not list2:
            return list1

        while list1 and list2:
            if list1.val >= list2.val:
                res.next = list2
                list2 = list2.next
            else:
                res.next = list1
                list1 = list1.next
            
            res = res.next
        
        if list1:
            res.next = list1
        
        if list2:
            res.next = list2
        
        return top.next