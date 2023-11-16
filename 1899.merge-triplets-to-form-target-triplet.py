#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#


# @lc code=start
class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        res = 0
        for triplet in triplets:
            found = 0
            for i, (a, b) in enumerate(zip(triplet, target)):
                if a == b:
                    found |= 2**i
                if a - b > 0:
                    found = 0
                    break
            res |= found
            if res == 7:
                return True
        return False


# @lc code=end
