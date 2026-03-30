from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        l = 0

        for r in range(len(s2)):
            window[s2[r]] += 1

            while r - l + 1 > len(s1):   # shrink
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1

            if window == need:  # update
                return True
        return False