class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        d = t = ListNode(0)      # dummy + tail
        while a and b:
            if a.val < b.val:
                t.next, a = a, a.next
            else:
                t.next, b = b, b.next
            t = t.next
        t.next = a or b
        return d.next
