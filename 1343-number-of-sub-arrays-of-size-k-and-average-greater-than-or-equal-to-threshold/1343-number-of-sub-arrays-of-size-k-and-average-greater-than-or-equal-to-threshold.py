class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:

        n = len(arr)

        c = 0

        if n < k:
            return -1

        window_sum = sum(arr[:k])

        # Check the first window
        if window_sum >= k * threshold:
            c += 1

        # Slide the window
        for i in range(n - k):

            window_sum = window_sum - arr[i] + arr[i + k]

            if window_sum >= k * threshold:
                c += 1

        return c