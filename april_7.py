class Solution:
    def maxDotProduct(self, n, m, a, b):
        dp = [[-1] * m for _ in range(n)]

        def help(i, j, diff):
            if i == n or j == m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            sum1, sum2 = 0, 0
            if diff:
                sum1 = help(i + 1, j, diff - 1)
            sum2 = a[i] * b[j] + help(i + 1, j + 1, diff)
            dp[i][j] = max(sum1, sum2)
            return dp[i][j]

        return help(0, 0, n - m)
