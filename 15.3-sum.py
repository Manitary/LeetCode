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
            if x > 0:
                break
            if i > 0 and x == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                n = x + nums[j] + nums[k]
                if n < 0:
                    j += 1
                elif n > 0:
                    k -= 1
                else:
                    new = [x, nums[j], nums[k]]
                    if not ans or ans[-1] != new:
                        ans.append(new)
                    j += 1
                    k -= 1

        return ans


# @lc code=end
