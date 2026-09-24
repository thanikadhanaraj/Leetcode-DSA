class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        n=len(arr)
        c=0
        if n<k:
            return -1
        window_sum=sum(arr[:k])
        if window_sum>=threshold*k:
                c+=1
       
        for i in range(n-k):
            window_sum=window_sum-arr[i]+arr[i+k]

            max_avg=window_sum/k
            if max_avg>=threshold:
                c+=1
        return c
        