# FUNCTIONS
def populate(num, puzz):
    """
    Populate square grid with the same number in it in all positions except for those already filled in the puzzle
    :param num: Number to put in all positions
    :param puzz: Current grid
    :return: Populated grid array
    """
    grid = []
    for i in range(9):
        grid.append([])
        for j in range(9):
            if puzz[i][j] == 0:
                grid[i].append(num)
            else:
                grid[i].append(0)
    return grid


def findrange(index):
    """
    Returns the other indices in the same 'box'
    :param index:
    :return:
    """
    start = (index)//3*3
    return list(range(start, start+3))

# printgrid - prints the 3d grid in an easy to see way
def printgrid(grid):
    """ Iterate over rows and columns to print out the grid """
    for row in grid:
        print(" ".join([str(x) for x in row]))


# cleargrid - clear possibilities by applying the:
# one in row, one in column, one in square grid rules
def cleargrid(pgrid, ogrid):
    for i in range(9):
        for j in range(9):
            n = ogrid[i][j]
            if n != 0:
                for k in range(9):
                    pgrid[n - 1][i][k] = 0  # clear row
                for k in range(9):
                    pgrid[n - 1][k][j] = 0  # clear column
                for k in findrange(i):
                    for l in findrange(j):
                        pgrid[n - 1][k][l] = 0  # clear box


# analysis - run analysis and see if we can update any results, using only the rule that the number of possibilities for a given position (i,j) is 1
def analysis(pgrid, ogrid):
    for i in range(9):
        for j in range(9):
            c = 0
            nu = 0
            for n in range(9):
                if pgrid[n][i][j] != 0:
                    c += 1
                    nu = n
            if c == 1:
                ogrid[i][j] = nu + 1  # apply result to grid
    return


# count the number of zeros in the main grid, so that we know when we're done
def countzero(ogrid):
    c = 0
    for x in range(len(grid)):
        c += ogrid[x].count(0)
    return c


def solve(grid):
    # populate 3d grid of possibilities
    dgrid = []
    for x in range(9):
        dgrid.append(populate(x + 1, grid))

    its = 0
    while countzero(grid) > 0 and its < 1000:
        cleargrid(dgrid, grid)
        analysis(dgrid, grid)
        its += 1

    return grid