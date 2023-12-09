# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2:ListNode) -> ListNode:
        head = ListNode(0)
        stepping = head
        carry = 0

        while l1 is not None or l2 is not None or carry!= 0:
            n1 = l1.val if l1 is not None else 0
            n2 = l2.val if l2 is not None else 0

            d = (n1 + n2 + carry)%10
            carry = (n1 + n2 + carry) // 10

            node = ListNode(d)
            stepping.next = node
            stepping = stepping.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        realHead = head.next
        head.next = None
        return realHead