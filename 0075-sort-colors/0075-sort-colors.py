class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        for i in range(n-1):
            m=nums[i]
            for j in range(i+1,n):
                if nums[j]<m:
                    m=nums[j]
            for j in range(i,n):
                if nums[j]==m:
                    nums[i],nums[j]=nums[j],nums[i]
               
