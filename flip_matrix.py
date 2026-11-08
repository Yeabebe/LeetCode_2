import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.remaining = self.total
        self.flipped = {}

    def flip(self) -> list[int]:
        r = random.randint(0, self.remaining - 1)

        x = self.flipped.get(r, r)

        self.remaining -= 1

        self.flipped[r] = self.flipped.get(self.remaining, self.remaining)

        return [x // self.n, x % self.n]

    def reset(self) -> None:
        self.remaining = self.total
        self.flipped.clear()