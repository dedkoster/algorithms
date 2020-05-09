# Lee algorithm: https://en.wikipedia.org/wiki/Lee_algorithm

import random

population = [0, -1]
weights = [0.4, 0.6]


def init_box(n):
    maze = [[0] * n for _ in range(n)]
    for i in [-1, 0]:
        maze[i] = [-1] * n
        for j in range(n - 1):
            maze[j][i] = -1
    for i in maze:
        print(i)
    return maze


def generate_maze(box):
    amt_walls_pnt = random.randint((len(box) - 2), (len(box) - 2) ** 2)
    print(random.randint(0, len(box) - 2))

    # Random puts internal walls
    for i in range(1, len(box) - 2):
        for j in range(1, len(box) - 2):
            if amt_walls_pnt != 0:
                cell = random.choices(population, weights)[0]
                if cell == -1:
                    amt_walls_pnt = amt_walls_pnt - 1
                    box[i][j] = -1
            else:
                break

    for i in box:
        print(i)


# TODO: Make to generate the random maze
# box = init_box(6)
# generate_maze(box)

my_maze = [[-1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, 0, -1],
           [-1, -1, 0, -1, 0, -1],
           [-1, -1, 0, 0, 0, -1],
           [-1, 0, 0, 0, 0, -1],
           [-1, -1, -1, -1, -1, -1]]

start_point = (1, 4)
end_point = (4, 1)

# while my_maze[4][1] == 0:
my_maze[start_point[0]][start_point[1]]


def wave_func(centroid):
    for i in range(centroid[0] - 1, centroid[0] + 2):
        for j in range(centroid[1] - 1, centroid[1] + 2):
            if (i == centroid[0] - 1) and (j == centroid[1] - 1):
                continue
            if (i == centroid[0] + 1) and (j == centroid[1] + 1):
                continue
            if (i == centroid[0] - 1) and (j == centroid[1] + 1):
                continue
            if (i == centroid[0] + 1) and (j == centroid[1] - 1):
                continue

            if my_maze[i][j] == -1 or (i == start_point[0] and j == start_point[1]):
                continue
            else:
                if my_maze[i][j] == 0:
                    my_maze[i][j] = my_maze[centroid[0]][centroid[1]] + 1


def wave_func_path(centroid):
    for i in range(centroid[0] - 1, centroid[0] + 2):
        for j in range(centroid[1] - 1, centroid[1] + 2):
            if (i == centroid[0] - 1) and (j == centroid[1] - 1):
                continue
            if (i == centroid[0] + 1) and (j == centroid[1] + 1):
                continue
            if (i == centroid[0] - 1) and (j == centroid[1] + 1):
                continue
            if (i == centroid[0] + 1) and (j == centroid[1] - 1):
                continue
            else:
                if my_maze[i][j] == (my_maze[centroid[0]][centroid[1]] - 1):
                    path.append((i, j))
                    break


# First walk around start point
wave_func(start_point)

# Lets wave begin
while my_maze[end_point[0]][end_point[1]] == 0:
    for i in range(1, len(my_maze) - 1):
        for j in range(1, len(my_maze) - 1):
            if my_maze[i][j] > 0:
                wave_func((i, j))

# plot wave works
for i in my_maze:
    print(i)

print()
path = []


def collect_path():
    path.append((end_point[0], end_point[1]))
    while my_maze[path[-1][0]][path[-1][1]] != 0:
        wave_func_path(path[-1])
    return path


print("Path:", collect_path())
