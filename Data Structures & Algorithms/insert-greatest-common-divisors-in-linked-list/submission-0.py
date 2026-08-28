# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        while dummy.next:
            currVal = dummy.val
            currNext = dummy.next
            currNextvalue = currNext.val
            gcdd = math.gcd(currVal,currNextvalue)
            gcdd = ListNode(gcdd)
            dummy.next = gcdd
            gcdd.next = currNext
            dummy = currNext
        return head


