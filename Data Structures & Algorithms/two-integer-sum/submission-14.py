class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my = {}
        for i,x in enumerate(nums):
            if target-x in my:
                return [my[target-x],i]
            my[x]= i
        return []