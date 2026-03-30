class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seen = set(nums)
        for num in nums:
            streak,curr = 0,num
            while curr in seen:
                streak += 1
                curr += 1
            res = max(res,streak)
        return res