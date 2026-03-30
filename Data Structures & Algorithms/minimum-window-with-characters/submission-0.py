from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = {}
        haveCount, needCount = 0, len(need)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            have[c] = 1 + have.get(c, 0)
            if c in need and have[c] == need[c]:
                haveCount += 1

            while haveCount == needCount:   # shrink
                if (r - l + 1) < resLen:
                    res, resLen = [l, r], r - l + 1
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    haveCount -= 1
                l += 1

        l, r = res
        return "" if resLen == float("inf") else s[l:r+1]
