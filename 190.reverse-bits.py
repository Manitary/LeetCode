#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans |= n & 1
            ans <<= 1
            n >>= 1
        return ans >> 1


# @lc code=end
