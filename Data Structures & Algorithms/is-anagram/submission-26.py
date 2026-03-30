class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        i,j = {},{}
        for x in range(len(s)):
            i[s[x]] = 1+i.get(s[x],0)
            j[t[x]] = 1+j.get(t[x],0)
        return i == j