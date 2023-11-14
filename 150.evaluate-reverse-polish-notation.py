#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#


# @lc code=start
import operator


def new_div(x: int, y: int) -> int:
    q, r = divmod(x, y)
    if q < 0 and r:
        q += 1
    return q


OP = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": new_div,
}


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []
        for token in tokens:
            if token in OP:
                b, a = stack.pop(), stack.pop()
                stack.append(OP[token](a, b))
                continue
            stack.append(int(token))
        return stack.pop()


# @lc code=end
