"""
Rules:
Any living cell with 2 or 3 neighbours lives
Any dead cell with 3 neigbours is born
Otherwise stay the same
"""

def generate_grid(n:int = 512)->list:
    return [[False for j in range(n)] for i in range(n)]

def print_grid(grid:list):
    for row in grid:
        for cell in row:
            print("1" if cell else "0", end = " ")
        print()

def surrounding(x:int, y:int, grid:list)->list:
    """Return (at most) eight neigbours of the given coordinate in the grid"""
    def lim_calc(a):
        if a == 0:
            return (0, 2)
        elif a == len(grid) - 1:
            return (len(grid) - 2, len(grid))
        else:
            return (a-1, a+2)
    y_min, y_max = lim_calc(y)
    x_min, x_max = lim_calc(x)

    cells = [[grid[j][i] for j in range(y_min, y_max)
              if not (j == y and i == x)]
             for i in range(x_min, x_max)]

    return [item for sublist in cells for item in sublist]

def tick_grid(grid: list)->list:
    new_grid = generate_grid(len(grid))
    for j in range(len(grid)):
        for i in range(len(grid)):
            cell = grid[j][i]
            living = len(list(filter(lambda x: x, surrounding(i, j, grid))))
            if cell and not (living == 2 or living == 3):
                cell = False
            elif (not cell) and (living == 3):
                cell = True
            new_grid[j][i] = cell
    return new_grid
