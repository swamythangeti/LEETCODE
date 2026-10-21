class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        freq={}
        sum=0
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for  key,value in freq.items():
            if value%k==0:
                sum+=value*key
        return sum
            
        