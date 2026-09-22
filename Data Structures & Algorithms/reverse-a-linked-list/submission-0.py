# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        trail = None
        while head.next:
            new_head = head.next
            head.next = trail
            trail = head
            head = new_head
        head.next = trail
        return head