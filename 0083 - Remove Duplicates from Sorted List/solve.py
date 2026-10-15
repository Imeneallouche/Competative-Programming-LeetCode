# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        r = head
        while r.next:
            if r.next.val==r.val:
                r.next=r.next.next
            else:
                r=r.next
        return head        