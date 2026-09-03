class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        groups = {}
        for char, count in freq.items():
            if count not in groups:
                groups[count] = []
            groups[count].append(char)
        best_freq = 0
        best_size = 0
        for count, chars in groups.items():
            if len(chars) > best_size or (
                len(chars) == best_size and count > best_freq
            ):
                best_size = len(chars)
                best_freq = count
        return ''.join(groups[best_freq])