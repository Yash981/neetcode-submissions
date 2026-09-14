# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        if length == n and head:
            return head.next
        if not head:
            return head
        index = length - n
        prev = head
        curr = head.next
        while index-1:
            prev = curr
            curr = curr.next
            index -= 1
        prev.next = curr.next
        return head
        
        
        