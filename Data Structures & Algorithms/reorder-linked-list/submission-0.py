# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        # init n, left and right
        n = 1
        left = head
        while head.next:
            n += 1
            head = head.next

        # cut left and right, in the middle
        mid_node_i = n - (n // 2)
        head = left
        i = 1
        while i < mid_node_i:
            i += 1
            head = head.next
        first_right = head.next
        head.next = None

        # reverse right
        right = self.reverseList(first_right)

        first_node = left

        # reorder
        while left and right:
            next_left = left.next                
            next_right = right.next
            left.next = right
            right.next = next_left

            left = next_left
            right = next_right
        
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