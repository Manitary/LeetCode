#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
ROMANS = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        for l, v in ROMANS.items():
            ans += l * (num // v)
            num %= v
        ans = ans.replace("CCCC", "CD")
        ans = ans.replace("DCD", "CM")
        ans = ans.replace("XXXX", "XL")
        ans = ans.replace("LXL", "XC")
        ans = ans.replace("IIII", "IV")
        ans = ans.replace("VIV", "IX")
        return ans


# @lc code=end
