# Ray algorithm for find path in maze

from random import choices

inf = float('inf')
ch = [inf, -1]
we = [0.7, 0.1]
n = 8


def create_maze():
    maze = []
    for i in range(n):
        maze.append([])
        for j in range(n):
            if i == 0 or i == n - 1:
                maze[i].append(-1)
            elif j == 0 or j == n - 1:
                maze[i].append(-1)
            else:
                rndm = choices(ch, we)
                maze[i].append(rndm[0])

    for k in range(1, n - 1):
        for j in range(1, n - 1):
            if k == j or j - k == 1:
                maze[k][j] = inf

    maze[1][1] = 0
    return maze


def ray(maze):
    d = 0
    myvar = 0
    virt_maze = maze[:]
    while virt_maze[len(virt_maze) - 2][len(virt_maze) - 2] == inf:
        vizited_d = sum(virt_maze, []).count(d)
        for i in range(len(virt_maze)):
            for j in range(len(virt_maze)):
                if virt_maze[i][j] != d:
                    continue
                if virt_maze[i][j + 1] == inf:  # RIGHT
                    d += 1
                    virt_maze[i][j + 1] = d
                    vizited_d = sum(virt_maze, []).count(d)
                    break
                if virt_maze[i - 1][j] == inf:  # UP
                    d += 1
                    virt_maze[i - 1][j] = d
                    vizited_d = sum(virt_maze, []).count(d)
                    break
                if virt_maze[i][j - 1] == inf:  # LEFT
                    d += 1
                    virt_maze[i][j - 1] = d
                    vizited_d = sum(virt_maze, []).count(d)
                    break
                if virt_maze[i + 1][j] == inf:  # BOTTOM
                    d += 1
                    virt_maze[i + 1][j] = d
                    vizited_d = sum(virt_maze, []).count(d)
                    break
                else:
                    if vizited_d >= 2:
                        vizited_d -= 1
                    if vizited_d < 2 and d != 0 or vizited_d == 0:
                        d -= 1
                    continue
    return virt_maze


lab = [[-1, -1, -1, -1, -1, -1, -1, -1]
    , [-1, 0, inf, inf, inf, inf, inf, -1]
    , [-1, inf, inf, inf, inf, inf, inf, -1]
    , [-1, -1, -1, inf, inf, inf, inf, -1]
    , [-1, inf, inf, inf, inf, inf, inf, -1]
    , [-1, inf, -1, inf, inf, inf, inf, -1]
    , [-1, inf, -1, inf, -1, inf, inf, -1]
    , [-1, -1, -1, -1, -1, -1, -1, -1]]

test1 = ray(lab)

for i in test1:
    print(i)
