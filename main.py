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


def cleargrid(pgrid, ogrid):
    """
    cleargrid - clear possibilities by applying the:
    one in row, one in column, one in square grid rules
    :param pgrid: possibility grid
    :param ogrid: solution grid
    :return:
    """
    for row in range(9):
        for col in range(9):
            val = ogrid[row][col]
            if val != 0:
                for k in range(9):
                    pgrid[val - 1][row][k] = 0  # clear row
                    pgrid[val - 1][k][col] = 0  # clear column
                for k in findrange(row):  # Box
                    for l in findrange(col):
                        pgrid[val - 1][k][l] = 0  # clear box


def analysis(pgrid, ogrid):
    """
    analysis - run analysis and see if we can update any results, using only the rule that the number of possibilities
    for a given position (i,j) is 1
    :param pgrid:
    :param ogrid:
    :return:
    """
    for row in range(9):
        for col in range(9):
            c = 0
            for poss in range(9):
                if pgrid[poss][row][col] != 0:
                    c += 1
                    nu = poss+1
            if c == 1:
                ogrid[row][col] = nu  # apply result to grid
    return

def analysis2(pgrid, ogrid):
    """
    Check all possibility grids to see if any of the possibilities are the only ones for the given box, row/column
    :param pgrid:
    :param ogrid:
    :return:
    """
    for index, grid in enumerate(pgrid):
        # Check each row
        num = index+1
        for rowidx, row in enumerate(grid):
            if row.count(num) == 1:
                ogrid[rowidx][row.index(num)] = num
        # Check each col
        for colidx in range(9):
            col = [row[colidx] for row in grid]
            if col.count(num) == 1:
                ogrid[col.index(num)][colidx] = num
        # Check each box
        for box in [
            [0,0],[0,3], [0,6],
            [3,0],[3,3], [3,6],
            [6,0],[6,3], [6,6]]:
            locs = []
            for rowidx in findrange(box[0]):
                for colidx in findrange(box[1]):
                    if grid[rowidx][colidx] != 0:
                        locs.append([rowidx, colidx])
            if len(locs) == 1:
                loc = locs[0]
                ogrid[loc[0]][loc[1]] = num

def countzero(ogrid):
    """
    count the number of zeros in the main grid, so that we know when we're done
    :param ogrid: Grid matrix to be assessed
    :return: count of zeros in grid cells
    """
    c = 0
    for x in range(len(ogrid)):
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