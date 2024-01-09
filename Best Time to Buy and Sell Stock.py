class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_day = 0
        right_day = 1
        max_profit = 0

        while right_day < len(prices):
            if prices[right_day] > prices[left_day]:
                max_profit = max(max_profit, prices[right_day] - prices[left_day])
            else:
                left_day = right_day
            right_day += 1
        return max_profit
            
