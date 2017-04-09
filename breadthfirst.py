from collections import deque
import numpy as np

def solve(maze):

    start = maze.start
    end = maze.end
    width = maze.width
    height = maze.height

    queue  = deque([start])
    visited = np.empty((height, width))
    visited.fill(False)
    prev = [[None for x in range(width)] for y in range(height)]
    #prev.fill(None)
    count = 0

    visited[start.y][start.x] = True
    completed = False

    while queue:
        count += 1
        current = queue.pop()

        if (current == end):
            completed = True

        for n in current.neighbours:
            if n != None:
                if visited[n.y][n.x] == False:
                    queue.appendleft(n)
                    visited[n.y][n.x] = True
                    prev[n.y][n.x] = current

    path = deque()
    current = end

    while current != None:
        path.appendleft(current)
        current = prev[current.y][current.x]

    return [path, [count, len(path), completed]]