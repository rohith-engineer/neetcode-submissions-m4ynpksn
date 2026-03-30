class Solution:
    def copyRandomList(self, head):
        if not head: return None
        # Step 1: Copy nodes and insert next to original
        curr = head
        while curr:
            nxt = curr.next
            curr.next = Node(curr.val)
            curr.next.next = nxt
            curr = nxt
        
        # Step 2: Copy random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Step 3: Separate lists
        curr = head
        copy = head.next
        res = copy
        while curr:
            curr.next = curr.next.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
            copy = copy.next
        return res
