class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n=len(nums)
        if n<k:
            return -1
        window_sum=sum(nums[:k])
        max_sum=window_sum
        
        for i in range(n-k):
            window_sum=window_sum-nums[i]+nums[i+k]
            max_sum=max(window_sum,max_sum)
        max_avg=float(max_sum/k)
        return max_avg
        