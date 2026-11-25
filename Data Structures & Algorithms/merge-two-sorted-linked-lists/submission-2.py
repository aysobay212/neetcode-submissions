# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        perhaps we can do this inplace?
        we will append everything to list1
        """
        prev1 = None
        prev2 = None
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr2.val < curr1.val:
                temp = curr2.next

                if prev1:
                    prev1.next = curr2
                else:
                    list1 = curr2  # New head of merged list

                curr2.next = curr1
                prev1 = curr2
                curr2 = temp

            else:
                prev1 = curr1
                curr1 = curr1.next
        
        # add any excess from list2 if required
        if curr2:
            # simply connect the tail of list1 to the start of curr2
            if prev1:
                prev1.next = curr2
            else:
                list1 = curr2
        
        return list1