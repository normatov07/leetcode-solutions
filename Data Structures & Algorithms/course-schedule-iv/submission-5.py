
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        indegree = [1] * numCourses
        adjList = [[] for _ in range(numCourses)]
        queue = deque()

        for a,b in prerequisites:
            adjList[a].append(b)
            indegree[b]+=1
        
        for i in range(numCourses):
            if indegree[i] == 1:
                queue.append(i)

        res = [False] * len(queries)
        preReq = defaultdict(set)
        while queue:
            current = queue.pop()
            for i in adjList[current]:
                preReq[i].add(current)
                preReq[i].update(preReq[current])
                indegree[i]-=1
                if indegree[i] == 1:
                    queue.append(i)
       



        return [pre in preReq[curr] for pre, curr in queries]
        

