class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        prev = {}

        for num in nums:
            curr = {}

            # Subarray containing only num
            rem = num % k
            curr[rem] = curr.get(rem, 0) + 1

            # Extend previous subarrays
            for r, count in prev.items():
                new_rem = (r * num) % k
                curr[new_rem] = curr.get(new_rem, 0) + count

            # Add all subarrays ending here
            for r, count in curr.items():
                result[r] += count

            prev = curr

        return result