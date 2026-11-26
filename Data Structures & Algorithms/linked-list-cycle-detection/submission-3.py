# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head # slow pointer
        p2 = head # fast pointer

        if p1 is None or p2 is None: # edge case of length < 2
            return False
            
        while p1.next and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True # cycle exists
            else:
                if p1 is None or p2 is None:
                    return False
        return False
        