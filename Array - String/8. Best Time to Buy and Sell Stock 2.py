class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy idea: if you have any chance to get any profit, TAKE IT
        max_prof = 0

        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                max_prof += (prices[i+1] - prices[i])

        return max_prof
