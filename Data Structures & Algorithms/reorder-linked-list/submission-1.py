# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        sec = slow.next
        slow.next = None
        while sec:
            sec.next,prev,sec = prev,sec,sec.next

        while prev:
            print(prev.val,head.val)
            head.next,prev.next,head,prev = prev, head.next,head.next,prev.next

        

