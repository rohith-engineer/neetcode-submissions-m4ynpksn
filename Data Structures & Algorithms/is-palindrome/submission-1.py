class Solution:
    def isPalindrome(self, s: str) -> bool:
        store = ''
        for c in s:
            if c.isalnum():
                store+=c.lower()
        return store == store[::-1]