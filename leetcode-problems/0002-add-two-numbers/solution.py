# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        iter = 0
        answer = ListNode(0)
        current = answer
        while l1 or l2 or carry:
            va1 = l1.val if l1 else 0
            va2 = l2.val if l2 else 0
            val = carry
            if va1 + va2 + carry>= 10:
                val += va1 + va2 - 10
                carry = 1
            else:
                val += va1 + va2
                carry = 0
            current.next = ListNode(val)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return answer.next

