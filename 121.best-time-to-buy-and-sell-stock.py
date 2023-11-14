#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 0
        best = 0
        while left <= right < len(prices):
            gain = prices[right] - prices[left]
            if gain < 0:
                left = right
                continue
            right += 1
            best = max(best, gain)

        return best


# @lc code=end
