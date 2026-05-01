# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_list = []
        while head:
            temp_list.append(head.val)
            head = head.next
        temp_list.pop(len(temp_list)-n)
        temp = ListNode()
        prev = temp        
        for val in temp_list:
            prev.next = ListNode(val)
            prev = prev.next
        return temp.next
