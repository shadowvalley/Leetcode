from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # S1 - Create adj list and indegree
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for (i, j) in prerequisites:
            adj[j].append(i)
            indegree[i] += 1

        # S3 - Add all nodes with indegree of 0 to queue
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # S4 - process queue elements
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            # check neighbors
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return True if len(topo) == numCourses else False
