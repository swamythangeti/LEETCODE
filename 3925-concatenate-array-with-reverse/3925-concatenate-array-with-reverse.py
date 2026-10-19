class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        arr = nums.copy()
        arr1 = arr[::-1]
        return arr + arr1