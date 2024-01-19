from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for (i,j) in prerequisites:
            adj[j].append(i)
            indegree[i] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
            
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            # change indegree of neighbours
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return topo if len(topo) == numCourses else []