#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#


# @lc code=start


def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            if is_palindrome(s[:i]):
                if i == len(s):
                    return s
                return s[len(s) - 1 : i - 1 : -1] + s
        return s[::-1] + s[1:]


# @lc code=end
