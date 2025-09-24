class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        r = a = ListNode(0, head)
        while a.next and a.next.next:
            b = a.next
            c = b.next
            a.next = c
            b.next = c.next
            c.next = b
            a = b
        return r.next
