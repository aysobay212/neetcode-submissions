# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev_node = None
        current_node = head # we start at the head of a LL
        next_node = None # temp storage of the next node
        # while we are not at the tail
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node # switching the link
            prev_node = current_node
            current_node = next_node
        return prev_node
        
        # when we are at the tail
        