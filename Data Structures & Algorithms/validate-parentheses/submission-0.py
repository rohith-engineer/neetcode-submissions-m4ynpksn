class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cp = {"(":")","[":"]","{":"}"}
        
        for i in s:
            if i in cp:  # opening bracket
                stack.append(cp[i])  # push expected closing
            else:  # closing bracket
                if not stack or stack[-1] != i:
                    return False
                stack.pop()
        
        return not stack