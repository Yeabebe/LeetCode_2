from collections import Counter

class Solution:
    def fourSumCount(
        self,
        nums1: list[int],
        nums2: list[int],
        nums3: list[int],
        nums4: list[int]
    ) -> int:
 
        count = Counter()

        # Store sums of nums1 + nums2
        for a in nums1:
            for b in nums2:
                count[a + b] += 1

        result = 0

        # Find matching sums from nums3 + nums4
        for c in nums3:
            for d in nums4:
                result += count[-(c + d)]

        return result