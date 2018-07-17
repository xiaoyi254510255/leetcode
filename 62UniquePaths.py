class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = []
        dp.append([1 for _ in range(m)])
        dp.append([1 for _ in range(m)])
        for i in range(n-1):
            for j in range(1,m):
                dp[(i+1) % 2][j] = dp[(i+1) %2][j-1] + dp[i % 2][j]
                
        return dp[ (n-1) % 2][m-1]
