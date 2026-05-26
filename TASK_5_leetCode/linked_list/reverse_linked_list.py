# Reverse Linked List
# Easy
# Topics
# Company Tags
# Hints
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:

# Input: head = [0,1,2,3]

# Output: [3,2,1,0]
# Example 2:

# Input: head = []

# Output: []
# Constraints:

# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = new_head
            new_head = current
            current = next_node
        return new_head
    

# короткая запись
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    new_head = None
    while head:
        head.next, new_head, head = new_head, head, head.next
    return new_head

# самый быстрый 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        if not head:
            return head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev