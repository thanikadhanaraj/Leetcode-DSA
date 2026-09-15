class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # dp[i] = minimum cuts needed for s[0:i]
        dp = list(range(n))

        for i in range(n):
            for j in range(i + 1):
                if s[j:i + 1] == s[j:i + 1][::-1]:
                    if j == 0:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[n - 1]