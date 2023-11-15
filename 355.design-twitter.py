#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#


# @lc code=start
from collections import defaultdict, deque


class Twitter:
    def __init__(self) -> None:
        self.tweet_ids: deque[tuple[int, int]] = deque()
        self.following: dict[int, set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_ids.appendleft((tweetId, userId))

    def getNewsFeed(self, userId: int) -> list[int]:
        tweets = filter(
            lambda t: t[1] == userId or t[1] in self.following[userId], self.tweet_ids
        )
        return [t[0] for t in filter(None, [next(tweets, None) for _ in range(10)])]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
