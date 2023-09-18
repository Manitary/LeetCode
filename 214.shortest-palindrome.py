#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#


# @lc code=start


def kmp(s: str) -> list[int]:
    ans = [0]
    for i in range(1, len(s)):
        t = ans[i - 1]
        while t > 0 and s[i] != s[t]:
            t = ans[t - 1]
        if s[i] == s[t]:
            t += 1
        ans.append(t)

    return ans


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        r = s[::-1]
        new = s + " " + r
        return r[: len(s) - kmp(new)[-1]] + s


# @lc code=end
