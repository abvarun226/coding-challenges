def sudoku2(grid):
    gridsize = len(grid)
    subgridsize = gridsize/3

    for x in grid:
        a = []
        for y in x:
            if y.isdigit() and y in a:
                return False
            a.append(y)
    for y in range(gridsize):
        a = []
        for x in range(gridsize):
            v = grid[x][y]
            if v.isdigit() and v in a:
                return False
            a.append(v)
    for x in range(0, gridsize, subgridsize):
        for y in range(0, gridsize, subgridsize):
            a = []
            for p in range(x, x+subgridsize):
                for q in range(y, y+subgridsize):
                    v = grid[p][q]
                    if v.isdigit() and v in a:
                        return False
                    a.append(v)
    return True

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
print(sudoku2(grid))