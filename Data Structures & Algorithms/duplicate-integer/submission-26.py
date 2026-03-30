class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my = set()
        for num in nums:
            if num in my:
                return True
            my.add(num)
        return False 