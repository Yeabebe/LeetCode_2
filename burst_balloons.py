class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrows = 0
        arrow_pos = float('-inf')

        for start, end in points:
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end

        return arrows