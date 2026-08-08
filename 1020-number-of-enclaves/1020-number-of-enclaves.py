class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        for i in range(n):
            if grid[i][0] == 1:
                queue.append((i, 0))
                grid[i][0] = 0
            if grid[i][m - 1] == 1:
                queue.append((i, m - 1))
                grid[i][m - 1] = 0
        for j in range(m):
            if grid[0][j] == 1:
                queue.append((0, j))
                grid[0][j] = 0
            if grid[n - 1][j] == 1:
                queue.append((n - 1, j))
                grid[n - 1][j] = 0
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < n and
                    0 <= nc < m and
                    grid[nr][nc] == 1):
                    grid[nr][nc] = 0
                    queue.append((nr, nc))
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
        return count