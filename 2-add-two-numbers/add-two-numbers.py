# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            # Get values
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Sum values 
            val = val1 + val2 + carry
            carry = val // 10 # Carry value to add in next operation
            val = val % 10    # Get ones place if it is a double digit for example
            curr.next = ListNode(val)

            # Update Pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next 
            
        return dummy.next 