class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0

        for bit in range(31):
            ones = sum((num >> bit) & 1 for num in nums)
            zeros = n - ones
            total += ones * zeros

        return total