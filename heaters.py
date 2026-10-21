from bisect import bisect_left
from typing import list

class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()
        radius = 0

        for house in houses:
            i = bisect_left(heaters, house)

            right = heaters[i] - house if i < len(heaters) else float('inf')
            left = house - heaters[i - 1] if i > 0 else float('inf')

            radius = max(radius, min(left, right))

        return radius