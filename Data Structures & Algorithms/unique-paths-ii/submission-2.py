class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        directions = [(1,0), (0, 1)]
        dp = [[-1 for _ in range(COL)] for _ in range(ROW)]

        def dfs(i:int, j:int):
            if i >= ROW or j >= COL:
                return 0

            if obstacleGrid[i][j] != 0:
                return 0
            
            if i == ROW-1 and j == COL-1:
                return 1

            if dp[i][j] >= 0:
                return dp[i][j]

            dp[i][j] = 0

            for id, jd in directions:
                dp[i][j] +=  dfs(id+i, jd+j)

            return dp[i][j]

       
        return dfs(0, 0)