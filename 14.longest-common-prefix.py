#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        for chars in zip(*strs):
            if len(s := set(chars)) > 1:
                return ans
            ans += s.pop()
        return ans


# @lc code=end
