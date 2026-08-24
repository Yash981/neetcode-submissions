# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        dummy = head
        while dummy:
            arr.append(dummy.val)
            dummy = dummy.next
        n = len(arr)
        quo = n//k
        rem = n%k
        ans = []
        index = 0
        while quo:
            ans.extend(arr[index:index+k][::-1])
            index += k
            quo -= 1
        # print(index)
        for x in range(index,n):
            ans.append(arr[x])
        # print(ans)
        dummy2 = ListNode(0)
        prev = dummy2
        for i in range(n):
            prev.next = ListNode(ans[i])
            prev = prev.next
        return dummy2.next