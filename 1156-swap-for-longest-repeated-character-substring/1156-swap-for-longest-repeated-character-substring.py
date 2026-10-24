class Solution:
    def maxRepOpt1(self, text: str) -> int:
        freq = Counter(text)
        n = len(text)
        ans = 0
        for ch in freq:
            left = 0
            count = 0
            for right in range(n):
                if text[right] == ch:
                    count += 1
                while right - left + 1 - count > 1:
                    if text[left] == ch:
                        count -= 1
                    left += 1
                ans = max(ans, min(right - left + 1, freq[ch]))
        return ans
