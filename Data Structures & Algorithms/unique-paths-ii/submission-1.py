class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        directions = [(1,0), (0, 1)]
        dp = [[-1 for _ in range(COL)] for _ in range(ROW)]

        def dfs(i:int, j:int):
            result = 0
           
            if obstacleGrid[i][j] != 0:
                return 0
            
            if i == ROW-1 and j == COL-1:
                return 1

            if dp[i][j] >= 0:
                return dp[i][j]

            obstacleGrid[i][j] = 1

            for id, jd in directions:
                if id+i < ROW and jd+j < COL and obstacleGrid[id+i][jd+j] == 0:
                    dp[id+i][jd+j] = dfs(id+i, jd+j)
                    result += dp[id+i][jd+j]

            obstacleGrid[i][j] = 0

            return result

        return dfs(0, 0)