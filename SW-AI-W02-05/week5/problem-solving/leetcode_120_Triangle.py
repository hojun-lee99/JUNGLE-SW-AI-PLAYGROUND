class Solution:
    def minimumTotal(self, triangle) -> int:
        dp = [[10001 for _ in range(len(triangle))] for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j-1 <0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j]) + triangle[i][j]
                elif j == i:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j]) + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
        return min(dp[len(triangle)-1])

s = Solution()

print(s.minimumTotal([[-1],[3,2],[1,-2,-1]]))