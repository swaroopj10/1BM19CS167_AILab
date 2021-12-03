def AStarSearch(Maze):
    open, closed = [[startPosition(M)]], [startPosition(M)]
    dest = destPosition(Maze)
    startpos = startPosition(Maze)
    print("Positions :")
    print("Start ->", startpos)
    print("Desitination -> ", dest)

    while len(open) > 0:
        path = open[0]
        destination = path[len(path) - 1]
        if Maze[destination[0]][destination[1]] == 'c':
            return path  

        open = open[1:]
        for cell in adjacentCells(destination, Maze):
            if cell not in closed:
                open = insert(path + [cell], open, dest)
        closed = closed + [destination]
    return None


def startPosition(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'm':
                return (i, j)


def destPosition(Maze):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'c':
                return (i, j)



def adjacentCells(destination, Maze):
    cells = []
    i, j = destination

    if(i > 0):
        if M[i - 1][j] != 'x':
            cells += [(i - 1, j)]
    if(j > 0):
        if M[i][j - 1] != 'x':
            cells += [(i, j - 1)]
    if(i < len(Maze) - 1):
        if M[i + 1][j] != 'x':
            cells += [(i + 1, j)]
    if(j < len(Maze) - 1):
        if M[i][j + 1] != 'x':
            cells += [(i, j + 1)]

    # print("Adjacent Cells: ", cells)
    return cells


def insert(path, open, dest):

    for i in range(0, len(open)):
        if len(path) + manhattanD(path[len(path) - 1], dest) <= len(open) + manhattanD(open[0][i], dest):
            return open[0:i] + [path] + open[i:len(open)]
    return open + [path]


def manhattanD(c1, c2):
    i1, j1 = c1
    i2, j2 = c2
    return abs(i1 - i2) + abs(j1 - j2)


R0 = ['m', 'o', 'o', 'o']
R1 = ['o', 'x', 'o', 'o']
R2 = ['x', 'o', 'o', 'x']
R3 = ['c', 'o', 'x', 'o']
M = [R0, R1, R2, R3]

print("Path to the destination: ", AStarSearch(M))