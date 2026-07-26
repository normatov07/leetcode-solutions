class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        adjList = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adjList[a].append(b)
        
        WHITE = 0
        GREEN = 1
        BLACK = 2

        color = [0] * numCourses
        res = []
        def dfs(i):
            nonlocal res
            if color[i] == GREEN:
                return False
            if color[i] == BLACK:
                return True
            
            color[i] = GREEN

            for j in adjList[i]:
                if not dfs(j):
                    return False
            
            color[i] = BLACK

            res.append(i)

            return True
        
        for i in range(numCourses):
            if color[i] == WHITE  and not dfs(i):
                return []
        
        return res
