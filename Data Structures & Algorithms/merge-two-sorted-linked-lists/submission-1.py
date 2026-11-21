# Definition for singly-linked list.
# class ListNode:
from types import new_class
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        pre_head = ListNode()
        head = pre_head
        while list1 or list2:
            if list1 and list2:
                smaller_node = min(list1, list2, key=lambda node: node.val)
            elif list1:
                smaller_node = list1
            else:
                smaller_node = list2

            temp = smaller_node
            smaller_node = smaller_node.next

            temp.next = None
            head.next = temp
            head = temp

            if head == list1:
                list1 = smaller_node
            else:
                list2 = smaller_node

        return pre_head.next