# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        # populate stack
        stack = []
        while head.next:
            stack.append(head)
            head = head.next
            stack[-1].next = None
        
        # reverse list
        new_head = head
        while stack:
            new_head.next = stack.pop()
            new_head = new_head.next

        return head