class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        maxlen = 0
        for r in range(len(s)):
            if s[r] in mp and mp[s[r]] >= l:
                l = mp[s[r]] + 1
            curr_len = r - l + 1
            maxlen = max(maxlen, curr_len)
            mp[s[r]] = r
        return maxlen