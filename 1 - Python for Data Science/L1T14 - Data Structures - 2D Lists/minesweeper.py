'''Create a function that takes a grid of # and -, where each hash (#) represents a
mine and each dash (-) represents a mine-free spot'''
def count_adjacent_mines(grid, row, col):
    # Determine the dicrections and define them to check the positions
    My_directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    count = 0
    for dr, dc in My_directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "#":  # initialize the minesweeper
            count += 1

    return str(count)

def generate_minesweeper_grid(grid):
    new_grid = []
    for row_idx, row in enumerate(grid):
        new_row = []
        for col_idx, cell in enumerate(row):
            if cell == "#":
                new_row.append("#")
            else:
                adjacent_mines = count_adjacent_mines(grid, row_idx, col_idx)
                new_row.append(adjacent_mines)
        new_grid.append(new_row)

    return new_grid

if __name__ == "__main__":
    grid = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]

    result_grid = generate_minesweeper_grid(grid)

    # Now Print the resultt
    for row in result_grid:
        print(" ".join(row))
