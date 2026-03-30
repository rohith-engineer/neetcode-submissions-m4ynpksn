class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            x,y = 0,num
            while y in store:
                x+=1
                y+=1
            res = max(res,x)
        return res