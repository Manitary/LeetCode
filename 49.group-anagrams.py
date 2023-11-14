#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams: list[list[str]] = []
        ans: list[list[str]] = []
        for s in strs:
            a = sorted(s)
            try:
                i = anagrams.index(a)
            except ValueError:
                anagrams.append(a)
                ans.append([s])
            else:
                ans[i].append(s)
        return ans


# @lc code=end
