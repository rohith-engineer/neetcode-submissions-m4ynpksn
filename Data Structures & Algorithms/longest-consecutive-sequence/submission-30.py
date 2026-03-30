class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        for i in nums:
            streak,cur= 0,i
            while cur in store:
                streak += 1
                cur += 1
            res = max(res,streak)
        return res