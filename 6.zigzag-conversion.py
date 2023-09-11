#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#


# @lc code=start
import itertools


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ""
        for i in range(numRows):
            if i in (0, numRows - 1):
                ans += s[i :: 2 * numRows - 2]
                continue
            ans += "".join(
                itertools.chain(
                    *itertools.zip_longest(
                        s[i :: 2 * numRows - 2],
                        s[2 * numRows - 2 - i :: 2 * numRows - 2],
                        fillvalue="",
                    )
                )
            )
        return ans


# @lc code=end
