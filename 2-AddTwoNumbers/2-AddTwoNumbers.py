# Last updated: 2/11/2026, 11:08:52 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res_pointer = res
        l1_pointer = l1
        l2_pointer = l2
        carry_over = 0

        while (l1_pointer is not None and l2_pointer is not None):
            total = l1_pointer.val + l2_pointer.val + carry_over
            if total>=10:
                carry_over = 1
                total -=10
            else:
                carry_over = 0
            res_pointer.next = ListNode(total)
            res_pointer = res_pointer.next
            l1_pointer = l1_pointer.next
            l2_pointer = l2_pointer.next

        while (l1_pointer is not None):
            total = l1_pointer.val + carry_over
            if total >=10:
                carry_over = 1
                total-=10
            else:
                carry_over = 0
            res_pointer.next = ListNode(total)
            res_pointer = res_pointer.next
            l1_pointer = l1_pointer.next

        while (l2_pointer is not None):
            total = l2_pointer.val + carry_over
            if total >=10:
                carry_over = 1
                total-=10
            else:
                carry_over = 0
            res_pointer.next = ListNode(total)
            res_pointer = res_pointer.next
            l2_pointer = l2_pointer.next

        if carry_over == 1:
            res_pointer.next = ListNode(1)

        return res.next
