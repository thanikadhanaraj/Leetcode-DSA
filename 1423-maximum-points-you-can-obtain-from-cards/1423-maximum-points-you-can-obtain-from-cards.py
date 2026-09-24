class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:

        n = len(cardPoints)

        total_sum = sum(cardPoints)

        window_size = n - k

        window_sum = sum(cardPoints[:window_size])

        min_window = window_sum

        for i in range(window_size, n):

            window_sum = window_sum - cardPoints[i - window_size] + cardPoints[i]

            min_window = min(min_window, window_sum)

        return total_sum - min_window