# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two Pointers Approach
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Put right pointer in correct position
        while n > 0:
            right = right.next
            n -= 1

        # Increment Both Pointers
        while right:
            left = left.next
            right = right.next  

        # Remove nth Pointer
        left.next = left.next.next

        return dummy.next