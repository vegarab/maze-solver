# Breadtfirst solving of the maze

from collections import deque
import numpy as np

def solve(maze):
    ''' Solves a maze using BFS. Returns the path and a
    list containing the No. nodes visited, length of the path and wether the
    maze was solved or not'''

    start = maze.start
    end = maze.end
    width = maze.width
    height = maze.height

    queue  = deque([start])
    visited = np.empty((height, width))
    visited.fill(False)
    prev = [[None for x in range(width)] for y in range(height)]
    count = 0

    visited[start.position[0]][start.position[1]] = True
    completed = False

    while queue:
        count += 1
        current = queue.pop()

        if (current == end):
            completed = True

        for n in current.neighbours:
            if n != None:
                if visited[n.position[0]][n.position[1]] == False:
                    queue.appendleft(n)
                    visited[n.position[0]][n.position[1]] = True
                    prev[n.position[0]][n.position[1]] = current

    path = deque()
    current = end

    while current != None:
        path.appendleft(current)
        current = prev[current.position[0]][current.position[1]]

    return [path, [count, len(path), completed]]

