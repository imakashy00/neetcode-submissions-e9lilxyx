# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_list = []
        curr = head
        while curr:
            node_list.append(curr.val)
            curr = curr.next
        k = 0
        j = len(node_list)-1
        new_list = [None] * len(node_list)
        for i in range(len(node_list)):
            if i & 1:
                new_list[i] = node_list[j]
                j -=1
            else :
                new_list[i] = node_list[k]
                k+=1
        tail = head
        for i in range(1,len(new_list)):
            tail.next = ListNode(new_list[i])
            tail = tail.next
        
        