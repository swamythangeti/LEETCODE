class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        for start in range(n):
            # Handle disconnected graphs
            if color[start] != -1:
                continue
            queue = deque([start])
            color[start] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    # Not colored yet
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    # Same color → not bipartite
                    elif color[neighbor] == color[node]:
                        return False
        return True