# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        temp = start
        carry = 0
        while l1 or l2:
            prev = ListNode()
            if l1 and l2:
                place_sum = l1.val + l2.val 
                prev.val = (place_sum + carry) % 10
                carry = place_sum // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                print(carry,l1.val)
                prev.val = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                print((l1.val + carry) % 10)
                l1 = l1.next
            elif l2:
                prev.val = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10
                l2 = l2.next
            temp.next = prev
            temp = temp.next
        if carry > 0 :
            temp.next = ListNode(carry,None) 
            
        return start.next

