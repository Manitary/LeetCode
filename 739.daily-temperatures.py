#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#


# @lc code=start


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack: list[tuple[int, int]] = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, idx = stack.pop()
                ans[idx] = i - idx
            stack.append((t, i))

        return ans


# @lc code=end
