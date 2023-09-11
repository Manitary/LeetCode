#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc code=start
def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return is_palindrome(str(x))


# @lc code=end
