#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match = re.search(needle, haystack)
        if not match:
            return -1
        return match.start()


# @lc code=end
