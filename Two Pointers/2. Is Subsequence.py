class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        n = 0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                n += 1
                i += 1
            j += 1

        return (True if n == len(s) else False)
    
#################################################
# Dynamic Programming Way, Just for Challenge ...
#################################################
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         def Sub(i, j):
#             if i == len(s) or j == len(t):
#                 return 0
#             choise1 = 0
#             choise2 = 0
#             if s[i] == t[j]:
#                 choise1 = Sub(i+1, j+1) + 1
#             else:
#                 choise2 = Sub(i, j+1)
#             return max(choise1,choise2)

#         return (True if Sub(0,0)!=None and Sub(0,0)==len(s) else False)
