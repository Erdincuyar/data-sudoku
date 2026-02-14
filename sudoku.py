# pylint: disable=missing-docstring


def sudoku_validator(grid):
    dogru_sira = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for row in grid:
        if sorted(row) != list(range(1,10)):
            return False
    for col in range(9):
        column_values = [grid[row][col] for row in range(9)]
        if sorted(column_values) != list(range(1,10)):
            return False
    for r in range(0,9,3):
        for c in range(0,9,3):
            blok = []
            for i in range(3):
                for j in range(3):
                    blok.append(grid[r + i][c + j])

            if sorted(blok) != list(range(1, 10)):
                return False
    return True
