class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        profits = [0]
        mini = prices[0]
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                mini = prices[i] if mini > prices[i] else mini
                mx = (prices[i+1] - mini)
            else:
                profits.append(mx)
                mx = 0

        return (max(profits) if max(profits)>mx else mx)



# [1]         # 0

# [1, 2]      # 1
# [2, 1]      # 0

# [1, 2, 3]   # 2
# [1, 3, 2]   # 2
# [2, 1, 3]   # 2
# [2, 3, 1]   # 1
# [3, 1, 2]   # 1
# [3, 2, 1]   # 0

