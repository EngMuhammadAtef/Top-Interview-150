class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic Prog: for getting maximum profit if you have chance to get profit, SAVE IT
        max_prof = 0
        profits = [0]
        min_price = prices[0]

        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                min_price = prices[i] if min_price > prices[i] else min_price
                max_prof = (prices[i+1] - min_price)
            else:
                profits.append(max_prof)
                max_prof = 0
                
        profits.append(max_prof)

        return (max(profits))



# [1]         # 0

# [1, 2]      # 1
# [2, 1]      # 0

# [1, 2, 3]   # 2
# [1, 3, 2]   # 2
# [2, 1, 3]   # 2
# [2, 3, 1]   # 1
# [3, 1, 2]   # 1
# [3, 2, 1]   # 0

