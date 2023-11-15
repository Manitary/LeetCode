#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#


# @lc code=start
from collections import defaultdict


class KeyData:
    def __init__(self) -> None:
        self.values: list[str] = []
        self.timestamps: list[int] = []

    def add_data(self, value: str, timestamp: int) -> None:
        self.values.append(value)
        self.timestamps.append(timestamp)

    def find_latest_timestamp_index(self, timestamp: int) -> int | None:
        ans = None
        left, right = 0, len(self.timestamps) - 1
        while left <= right:
            middle = (left + right) // 2
            if self.timestamps[middle] <= timestamp:
                ans = middle
                left = middle + 1
            else:
                right = middle - 1

        return ans

    def return_latest_value_at_timestamp(self, timestamp: int) -> str:
        timestamp_index = self.find_latest_timestamp_index(timestamp)
        if timestamp_index is None:
            return ""
        return self.values[timestamp_index]


class TimeMap:
    def __init__(self) -> None:
        self.data: dict[str, KeyData] = defaultdict(KeyData)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].add_data(value, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        return self.data[key].return_latest_value_at_timestamp(timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
