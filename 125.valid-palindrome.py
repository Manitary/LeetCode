#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while 0 <= left < right < len(s):
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if not s[left].lower() == s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# @lc code=end
