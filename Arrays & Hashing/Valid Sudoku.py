class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Question Link: https://leetcode.com/problems/valid-sudoku/
        Intution: It iterates through the board while maintaining three defaultdicts to track the values seen in rows, columns, and 3x3 squares.
        For each cell in the board, it checks if the value already exists in the corresponding row, column, or square.
        If a duplicate value is found, it returns False indicating an invalid Sudoku.
        Otherwise, it continues checking and updating the defaultdicts with the encountered values.
        If the loop completes without finding any duplicates, the Sudoku board is considered valid, and the function returns True.
        """
        # Create empty defaultdicts to store values in sub-lists
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        square = collections.defaultdict(list)

        # Iterate over the board to validate the Sudoku
        for i in range(len(board)):
            for j in range(len(board[i])):
                # Skip the empty values
                if board[i][j] == ".":
                    continue

                # Check for duplicates in rows, columns, and squares
                if (
                    board[i][j] in rows[i]
                    or board[i][j] in cols[j]
                    or board[i][j] in square[(i // 3, j // 3)]
                ):
                    return False

                # Append the value to the corresponding defaultdicts
                cols[j].append(board[i][j])
                square[(i // 3, j // 3)].append(board[i][j])
                rows[i].append(board[i][j])

        return True
