class Solution:
    def isValid(self, s: str) -> bool:
        h = {'(':')', 
            '{':'}', 
            '[':']'}
        stack = []

        for i in range(len(s)):
            if s[i] in h.keys():
                stack.append(s[i])

            elif s[i] in h.values():
                if len(stack) == 0:
                    return False
                else:
                    if s[i] == h[stack[-1]]:
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:               
            return True
        return False