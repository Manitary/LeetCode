#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans: list[list[int]] = []
        nums = sorted(nums)
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                n = x + nums[j] + nums[k]
                if n < 0:
                    j += 1
                    while j < k - 1 and nums[j] == nums[j - 1]:
                        j += 1
                elif n > 0:
                    k -= 1
                    while j + 1 < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1] and nums[k] == nums[k + 1]:
                        j += 1
                        k -= 1

        return ans


# @lc code=end
