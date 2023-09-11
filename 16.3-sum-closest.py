#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#


# @lc code=start


def sign(n: int) -> int:
    return n and (-1 if n < 0 else 1)


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        best = float("inf")
        ans = 0
        nums.sort()
        for i, x in enumerate(nums):
            if i > 0:
                if x > target > 0:
                    break
                if x == nums[i - 1]:
                    continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                n = x + nums[j] + nums[k]
                if target > n:
                    j += 1
                elif target < n:
                    k -= 1
                else:
                    return n
                if (d := abs(target - n)) < best:
                    best = d
                    ans = n
        return ans


# @lc code=end
