# Depthfirst solving of the maze

from collections import deque

def solve(maze):
    start = maze.start
    end = maze.end
    width = maze.width
    stack = deque([start])
    shape = (maze.height, maze.width)
    prev = [None] * (maze.width * maze.height)
    visited = [False] * (maze.width * maze.height)
    count = 0

    completed = False
    while stack:
        count += 1
        current = stack.pop()

        if current == end:
            completed = True
            break

        visited[current.position[0] * width + current.position[1]] = True

        for n in current.neighbours:
            if n != None:
                npos = n.position[0] * width + n.position[1]
                if visited[npos] == False:
                    stack.append(n)
                    prev[npos] = current

    path = deque()
    current = end
    while (current != None):
        path.appendleft(current)
        current = prev[current.position[0] * width + current.position[1]]

    return [path, [count, len(path), completed]]
