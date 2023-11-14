#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#


# @lc code=start

from typing import NamedTuple

Car = NamedTuple("Car", [("position", int), ("speed", int)])


def get_fleet(cars: list[Car], target: int) -> None:
    car = cars.pop()
    if not cars:
        return
    next_car = cars[-1]
    if next_car.speed <= car.speed:
        return
    catch_up_time = (car.position - next_car.position) / (next_car.speed - car.speed)
    catch_up_position = car.position + (car.speed) * catch_up_time
    if catch_up_position > target:
        return
    cars[-1] = car
    get_fleet(cars, target)


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [Car(*x) for x in sorted(zip(position, speed))]
        ans = 0

        while cars:
            get_fleet(cars, target)
            ans += 1

        return ans


# @lc code=end
