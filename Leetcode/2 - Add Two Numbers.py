# Definition for singly-linked list.
# (was just a comment in leetcode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        result = ListNode()
        current = result
        carry = 0

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total_sum = a + b + carry
            carry, value = divmod(total_sum, 10)

            result_node = ListNode(value)
            current.next = result_node
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return result.next
