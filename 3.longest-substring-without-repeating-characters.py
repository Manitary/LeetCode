#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        visited: set[str] = set()
        left, right = 0, 0
        while left <= right < len(s):
            if s[right] in visited:
                ans = max(ans, right - left)
                visited.remove(s[left])
                left += 1
                continue
            visited.add(s[right])
            right += 1
        ans = max(ans, right - left)
        return ans


# @lc code=end
