#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#


# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        charset = [0] * 26
        for i, c in enumerate(s):
            charset[ord(c) - ord("A")] += 1
            while i - left + 1 - max(charset) > k:
                charset[ord(s[left]) - ord("A")] -= 1
                left += 1
            ans = max(ans, i - left + 1)

        return ans


# @lc code=end
