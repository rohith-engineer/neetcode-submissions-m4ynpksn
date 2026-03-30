from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists):
        heap = []
        for i, node in enumerate(lists):
            if node: heappush(heap, (node.val, i, node))
        dummy = curr = ListNode(0)
        while heap:
            val, i, node = heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        return dummy.next
