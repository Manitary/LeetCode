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

        for length in range(len(s), 0, -1):
            for left in range(len(s) - length + 1):
                if is_palindrome(left, left + length - 1):
                    return s[left : left + length]
        raise ValueError("Answer not found")


# @lc code=end
