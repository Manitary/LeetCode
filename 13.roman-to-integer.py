#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
VALUES = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for c, v in VALUES.items():
            if s.startswith(c):
                while s.startswith(c):
                    ans += v
                    s = s[len(c) :]
        return ans


# @lc code=end
