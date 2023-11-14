#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        visited: set[int] = set()
        for x in nums:
            if x in visited:
                return True
            visited.add(x)
        return False


# @lc code=end
