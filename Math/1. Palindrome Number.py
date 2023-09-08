class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        i = 0
        while i <= (len(str_x)-2)//2:
            if str_x[i] != str_x[len(str_x)-i-1]:
                return False
            i += 1
        return True