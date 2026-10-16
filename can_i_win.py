from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if total < desiredTotal:
            return False

        if maxChoosableInteger >= desiredTotal:
            return True

        @lru_cache(None)
        def can_win(used: int, remaining: int) -> bool:
            for num in range(1, maxChoosableInteger + 1):
                bit = 1 << num

                if used & bit:
                    continue

                if num >= remaining:
                    return True

                if not can_win(used | bit, remaining - num):
                    return True

            return False

        return can_win(0, desiredTotal)