from typing import List


class NQueensSolver:
    def __init__(self, n: int):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("N must be a positive integer")

        self.n = n
        self.board = [['.' for _ in range(n)] for _ in range(n)]  # Initialize the board
        self.solutions: List[List[str]] = []     

        # O(1) checking sets
        self.cols = set()
        self.diag1 = set()  # row - col
        self.diag2 = set()  # row + col
    # solve 
    def solve(self) -> List[List[str]]:
        self._backtrack(0)      
        return self.solutions
    # backtrack
    def _backtrack(self, row: int):
        if row == self.n:
            self.solutions.append(self._format_solution())  # backtrack check
            return

        for col in range(self.n):
            if self._is_safe(row, col): 
                self._place(row, col)
                self._backtrack(row + 1)
                self._remove(row, col)

    def _is_safe(self, row: int, col: int) -> bool:
        return (
            col not in self.cols and
            (row - col) not in self.diag1 and
            (row + col) not in self.diag2
        )

    def _place(self, row: int, col: int):
        self.board[row][col] = 'Q'
        self.cols.add(col)
        self.diag1.add(row - col)
        self.diag2.add(row + col)
    # remove board
    def _remove(self, row: int, col: int):
        self.board[row][col] = '.'
        self.cols.remove(col)
        self.diag1.remove(row - col)
        self.diag2.remove(row + col)

    def _format_solution(self) -> List[str]:
        return [''.join(row) for row in self.board]