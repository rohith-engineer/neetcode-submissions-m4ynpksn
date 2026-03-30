from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # store indexes
        res = []
        l = 0

        for r in range(len(nums)):
            # maintain decreasing deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()

            if r - l + 1 >= k:   # window valid
                res.append(nums[q[0]])
                l += 1
        return res
