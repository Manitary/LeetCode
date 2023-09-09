#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        visited: dict[str, int] = {}
        for i, c in enumerate(s):
            if c in visited:
                ans = max(ans, len(visited))
                visited = {k: v for k, v in visited.items() if v > visited[c]}
            visited[c] = i
        ans = max(ans, len(visited))
        return ans


# @lc code=end
