def print_grid(grid):
    print("-----------------------------------")
    for i in range(3):
        for j in range(3):
            print_line(grid[(i * 3) + j])
        print("-----------------------------------")


def print_line(grid):
    print("| " + str(grid[0]) + "  " + str(grid[1]) + "  " + str(grid[2]) +
          "  |  " + str(grid[3]) + "  " + str(grid[4]) + "  " + str(grid[5]) +
          "  |  " + str(grid[6]) + "  " + str(grid[7]) + "  " + str(grid[8]) +
          " |")


def validateNumber(grid, number, posX, posY):
    for i in range(9):
        if grid[posY][i] == number and posX != i:
            return False
        if grid[i][posX] == number and posY != i:
            return False
    quadrantX = posX // 3
    quadrantY = posY // 3
    for j in range(3):
        for k in range(3):
            if grid[(quadrantY * 3) + j][(quadrantX * 3) + k] == number and ((quadrantX * 3) + k) != posX and ((quadrantY * 3) + j) != posY:
                return False
    return True


def findNumber(grid, posX, posY):
    for i in range(9):
        if validateNumber(grid, i + 1, posX, posY):
            grid[posY][posX] = i + 1
            if not solve_sudoku(grid):
                grid[posY][posX] = 0
            else:
                return True
    return False


def solve_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return findNumber(grid, j, i)

    return True


if __name__ == "__main__":

    grid = [[0 for x in range(9)] for y in range(9)]
    # Driver Code
    # grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
    #         [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #         [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #         [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #         [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #         [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #         [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    grid = [[8, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0], 
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0], 
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8], 
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0]]

    print_grid(grid)
    if (solve_sudoku(grid)):
        print_grid(grid)
    else:
        print("No solution exists")