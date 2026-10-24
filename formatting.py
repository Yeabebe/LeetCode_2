class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()

        first_group = len(s) % k
        result = []

        if first_group:
            result.append(s[:first_group])

        for i in range(first_group, len(s), k):
            result.append(s[i:i + k])

        return '-'.join(result)