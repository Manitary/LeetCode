#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#


# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # this function alone doesn't always work due to how Python represents integers
        def positive_sum(x: int, y: int) -> int:
            carry = x & y
            if not carry:
                return x ^ y
            return positive_sum(x ^ y, carry << 1)

        if a * b >= 0:
            return positive_sum(a, b)

        if a > 0:
            return self.getSum(a=b, b=a)

        # a<0
        # ~a = -a-1 -> +(~a, 1) = -a > 0

        # -a = b
        if positive_sum(~a, 1) == b:
            return 0

        # -a < b
        if positive_sum(~a, 1) < b:
            # +(~(+(~a, 1), +(~b, 1)), 1)
            # = +(~(-a,-b), 1)
            # = -(-a-b)
            # = a+b
            return positive_sum(
                ~positive_sum(positive_sum(~a, 1), positive_sum(~b, 1)), 1
            )

        # -a > b
        return positive_sum(a, b)


# @lc code=end
