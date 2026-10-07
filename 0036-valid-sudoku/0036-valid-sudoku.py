class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue

                num = board[i][j]

                # Check row
                if num in rows[i]:
                    return False

                # Check column
                if num in cols[j]:
                    return False

                # Find the 3 x 3 box
                box = (i // 3) * 3 + (j // 3)

                # Check box
                if num in boxes[box]:
                    return False

                # Add number to row, column and box
                rows[i].add(num)
                cols[j].add(num)
                boxes[box].add(num)
        return True