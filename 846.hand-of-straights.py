#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#


# @lc code=start
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        cards = Counter(hand)
        for card in sorted(cards.keys()):
            if cards[card] < 0:
                return False
            if cards[card] == 0:
                continue
            num = cards[card]
            for c in range(card, card + groupSize):
                if c not in cards:
                    return False
                cards[c] -= num
        return True


# @lc code=end
