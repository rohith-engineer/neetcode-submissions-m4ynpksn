class Solution:
    def reverseKGroup(self, head, k):
        def reverse(a, b):
            prev, curr = None, a
            while curr != b:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        a = b = head
        for _ in range(k):
            if not b: return head
            b = b.next
        new_head = reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head
