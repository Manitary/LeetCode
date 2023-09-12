#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#


# @lc code=start
def sorted_three_sum(nums: list[int], target: int) -> list[list[int]]:
    ans: list[list[int]] = []
    for i, x in enumerate(nums):
        if x > target > 0:
            break
        if i > 0 and x == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            n = x + nums[j] + nums[k]
            if n < target:
                j += 1
            elif n > target:
                k -= 1
            else:
                new = [x, nums[j], nums[k]]
                if not ans or ans[-1] != new:
                    ans.append(new)
                j += 1
                k -= 1

    return ans


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans: list[list[int]] = []
        nums.sort()
        for i, x in enumerate(nums):
            if x > target > 0:
                break
            if i > 0 and x == nums[i - 1]:
                continue
            ans.extend([[x] + t for t in sorted_three_sum(nums[i + 1 :], target - x)])
        return ans


# @lc code=end
