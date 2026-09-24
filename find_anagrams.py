from typing import List  

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        window = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        result = []
        left = 0

        for right in range(len(s)):
            window[ord(s[right]) - ord('a')] += 1

            # Keep window size equal to len(p)
            if right - left + 1 > len(p):
                window[ord(s[left]) - ord('a')] -= 1
                left += 1

            # Same character frequencies => anagram
            if window == p_count:
                result.append(left)

        return result