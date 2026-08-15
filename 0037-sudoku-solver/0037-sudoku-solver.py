from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Sets to store numbers already present
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # -------------------------------
        # Step 1: Initialize the sets
        # -------------------------------
        for i in range(9):
            for j in range(9):

                if board[i][j] != ".":

                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])

                    box = (i // 3) * 3 + (j // 3)
                    boxes[box].add(board[i][j])

        # -------------------------------
        # Step 2: Backtracking Function
        # -------------------------------
        def solve():

            # Traverse the board
            for i in range(9):
                for j in range(9):

                    # Find an empty cell
                    if board[i][j] == ".":

                        box = (i // 3) * 3 + (j // 3)

                        # Try digits 1-9
                        for ch in "123456789":

                            # Check if digit is valid
                            if (ch not in rows[i] and
                                ch not in cols[j] and
                                ch not in boxes[box]):

                                # ------------------
                                # Choose
                                # ------------------
                                board[i][j] = ch

                                rows[i].add(ch)
                                cols[j].add(ch)
                                boxes[box].add(ch)

                                # ------------------
                                # Explore
                                # ------------------
                                if solve():
                                    return True

                                # ------------------
                                # Backtrack
                                # ------------------
                                board[i][j] = "."

                                rows[i].remove(ch)
                                cols[j].remove(ch)
                                boxes[box].remove(ch)

                        # No number works
                        return False

            # Sudoku solved
            return True

        # Start solving
        solve()