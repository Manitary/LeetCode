#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        ans = ""
        for l, _ in enumerate(s):
            if len(s) - l < len(ans):
                break
            for r in range(len(s), l + len(ans), -1):
                if is_palindrome(l, r - 1):
                    if r - l > len(ans):
                        ans = s[l:r]
                    break
        return ans


# @lc code=end
