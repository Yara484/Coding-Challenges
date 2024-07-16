# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Split list using two pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        # Reverse Second List
        prev, curr = None, head2
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # prev is the new head of list 2
        head1 = head
        head2 = prev

        # Merge two lists
        while head2:
            tmp1 = head1.next
            tmp2 = head2.next

            head1.next = head2
            head2.next = tmp1

            head1 = tmp1
            head2 = tmp2

                        