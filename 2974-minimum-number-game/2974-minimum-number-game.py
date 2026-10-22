class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        nums.sort()
        n=len(nums)
        i,j=0,1
        while i <n and j<n:
            arr.append(nums[j])
            arr.append(nums[i])
            i+=2
            j+=2
        return arr
