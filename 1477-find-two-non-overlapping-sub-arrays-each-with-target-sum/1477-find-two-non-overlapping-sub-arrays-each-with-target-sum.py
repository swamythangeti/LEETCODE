class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        # dp[i] = minimum length of a valid subarray
        # completely inside arr[0...i]
        dp = [float('inf')] * n

        left = 0
        curr_sum = 0
        ans = float('inf')
        best = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Previous subarray must end before left
                if left > 0 and dp[left - 1] != float('inf'):
                    ans = min(ans, length + dp[left - 1])

                best = min(best, length)

            dp[right] = best

        return -1 if ans == float('inf') else ans