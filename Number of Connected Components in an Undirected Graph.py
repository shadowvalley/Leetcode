class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list representation of the graph
        adj = [[] for i in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = [False]*n
        componentCount = 0
        for i in range(n):
            if not visited[i]:
                componentCount += 1
                self.dfs(i, visited, adj)
        return componentCount

    def dfs(self, src, visited, adj):
        visited[src] = True

        # traverse neighbours
        for neighbour in adj[src]:
            if not visited[neighbour]:
                self.dfs(neighbour, visited, adj)
        