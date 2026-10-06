from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        return ''.join(
            char * freq
            for char, freq in sorted(
                count.items(),
                key=lambda x: x[1],
                reverse=True
            )
        )