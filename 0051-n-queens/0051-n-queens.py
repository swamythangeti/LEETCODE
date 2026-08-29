class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        posDiag = set()      # row + col
        negDiag = set()      # row - col
        def solve(row):
            # Base Case
            if row == n:
                temp = ["".join(r) for r in board]
                ans.append(temp)
                return
            for col in range(n):
                if (col in cols or
                    (row + col) in posDiag or
                    (row - col) in negDiag):
                    continue
                # Choose
                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                board[row][col] = "Q"
                # Explore
                solve(row + 1)
                # Backtrack
                board[row][col] = "."
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
        solve(0)
        return ans