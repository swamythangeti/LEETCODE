class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        count_p = [0] * 26
        count_s = [0] * 26
        for ch in p:
            count_p[ord(ch) - ord('a')] += 1
        result = []
        k = len(p)
        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            if i >= k:
                count_s[ord(s[i - k]) - ord('a')] -= 1
            if count_s == count_p:
                result.append(i - k + 1)
        return result