from typing import list     

class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        minutes = []

        for t in timePoints:
            h, m = map(int, t.split(':'))
            minutes.append(h * 60 + m)

        minutes.sort()

        result = 1440 - minutes[-1] + minutes[0]

        for i in range(1, len(minutes)):
            result = min(result, minutes[i] - minutes[i - 1])

        return result