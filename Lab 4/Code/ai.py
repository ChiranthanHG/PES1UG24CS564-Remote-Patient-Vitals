from board import Board, COLS


class AI:
    def choose_column(self, board):
        legal_columns = [
            col for col in range(COLS)
            if board.grid[0][col] == "."
        ]

        if not legal_columns:
            return None

        # 1. Try to win immediately
        for col in legal_columns:
            test_board = self.copy_board(board)

            if test_board.drop(col, "O") is not None:
                if test_board.winner("O"):
                    return col

        # 2. Block the opponent's immediate win
        for col in legal_columns:
            test_board = self.copy_board(board)

            if test_board.drop(col, "X") is not None:
                if test_board.winner("X"):
                    return col

        # 3. Otherwise choose the first legal column
        return legal_columns[0]

    def copy_board(self, board):
        new_board = Board()
        new_board.grid = [row[:] for row in board.grid]
        return new_board