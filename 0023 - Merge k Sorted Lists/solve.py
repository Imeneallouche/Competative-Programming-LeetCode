
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        h = []
        
        # Add the first node of each non-empty list.
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))
        
        dummy = ListNode(0)
        tail = dummy
        
        while h:
            _, i, node = heapq.heappop(h)
            
            # Append the smallest node to the result.
            tail.next = node
            tail = node
            
            # Add the next node from the same list.
            if node.next:
                heapq.heappush(
                    h, (node.next.val, i, node.next)
                )
        
        tail.next = None
        return dummy.next
