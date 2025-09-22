class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        r = c = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                c.next = l1
                l1, c = l1.next, l1
            else:
                c.next = l2
                l2, c = l2.next, l2
        c.next = l1 if l1 else l2
        return r.next