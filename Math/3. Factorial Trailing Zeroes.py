class Solution:
    def trailingZeroes(self, n: int) -> int:
        sys.set_int_max_str_digits(0)

        def fact(n):
            if n == 0 or n == 1:
                return 1
            return n * fact(n-1)

        res = str(fact(n))
        count = 0

        for i in range(len(res)-1, -1, -1):
            if res[i] == '0':
                count+=1
            else:
                break

        return count