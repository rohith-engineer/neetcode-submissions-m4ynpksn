class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        for num in nums:
            i,j = 0,num
            while j in store:
                i+=1
                j+=1
            res = max(res,i)
        return res