class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx,rlen = 0,0
        n = len(s)
        dp =[[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if rlen<(j-i+1):
                        resIdx = i
                        rlen = j-i+1
        return s[resIdx:resIdx+rlen]
        