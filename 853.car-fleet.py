#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#


# @lc code=start


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        arrival_time_stack: list[float] = []
        for car_position, car_speed in cars:
            arrival_time_stack.append((target - car_position) / car_speed)
            if (
                len(arrival_time_stack) >= 2
                and arrival_time_stack[-1] <= arrival_time_stack[-2]
            ):
                arrival_time_stack.pop()
        return len(arrival_time_stack)


# @lc code=end
