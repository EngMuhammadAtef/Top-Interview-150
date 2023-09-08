# Dynamic programming (Top-Down Approach)
class Solution:
    fib = [-1]*1000

    def climbStairs(self,n):
        if n==0 or n==1:
            return 1

        if self.fib[n]!=-1:
            return self.fib[n]

        self.fib[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.fib[n]


# Dynamic programming (Bottom-Up Approach)
class Solution:
    def climbStairs(self, n: int) -> int:
        n += 1
        stairs = [-1]*100       # Constraints: 1 <= n <= 45
        
        for i in range(1, n+1):
            if i == 1 or i == 2:
                stairs[i] = 1
            if stairs[i] == -1:
                stairs[i] = stairs[i-1] + stairs[i-2]

        return stairs[i]
