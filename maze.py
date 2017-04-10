# MAZE-object with Nodes in a graph, representing the paths in the maze

import numpy as np
class Maze:
    class Node:
        def __init__(self, position):
            self.position = position # position = (y,x)
            self.neighbours = [None, None, None, None] # top, right, bot, left

        def addNeighbour(self, pos, node):
            # top
            if pos == 0:
                self.neighbours[0] = node
                node.neightbours[2] = self
            # right
            elif pos == 1:
                self.neighbours[1] = node
                node.neighbours[3] = self
            # bot
            elif pos == 2:
                self.neighbours[2] = node
                node.neighbours[0] = self
            # left
            elif pos == 3:
                self.neighbours[3] = node
                node.neighbours[1] = self

        def __str__(self):
            return str(self.position)

        def __repr__(self):
            return str(self.position)

    ### END OF NODE CLASS ###

    def __init__(self, im):
        width, height = im.size
        data = list(im.getdata()) # list of pixels, 0 = black, 1 = white
        data = self.buildMatrix(width, height, data) # create a 2d array
        self.buildMaze(width, height, data) # create nodes and set start/end

    def buildMaze(self, width, height, data):

        # first and end-node
        self.start = None
        self.end = None

        # for search algorithm
        self.width = width
        self.height = height

        # count of nodes
        self.nodeCount = 0

        # nodes above current row
        topNodes = [None] * width # +1 bcs for's are !0-indexed

        # find start node
        for i in range(1, width-1):
            if data[0][i] == 1:
                self.start = Maze.Node((0, i))
                self.nodeCount += 1
                topNodes[i] = self.start # add start node to topNodes at pos
                break

        for y in range(1, height-1): # 1 and -1 to exclude last and first row
            # node left of current
            left = None

            for x in range(1, width-1): # 1 to exclude left wall

                n = None
                # if on wall, set topNode to none, then cont
                if data[y][x] < 1:
                    continue

                # PATH PATH PATH (corridor)
                if data[y][x-1] > 0 and data[y][x+1] > 0:
                    # create node if path above or below
                    if data[y-1][x] > 0 or data[y+1][x] > 0:
                        n = Maze.Node((y, x))
                        self.nodeCount += 1
                        left.addNeighbour(1, n)
                        left = n

                # WALL PATH PATH (start of corridor)
                elif data[y][x-1] < 1 and data[y][x+1] > 0:
                    # create node
                    n = Maze.Node((y, x))
                    self.nodeCount += 1
                    left = n

                # PATH PATH WALL (end of corridor)
                elif data[y][x-1] > 0 and data[y][x+1] < 1:
                    # create node
                    n = Maze.Node((y, x))
                    self.nodeCount += 1
                    left.addNeighbour(1, n)
                    left = None

                # WALL PATH WALL (dead end)
                elif data[y][x-1] < 1 and data[y][x+1] < 1:
                    # create node if nothing below or above
                    if data[y+1][x] < 1 or data[y-1][x] < 1:
                        n = Maze.Node((y, x))
                        self.nodeCount += 1

                # check topNodes
                if n != None:
                    # if node at top
                    if data[y-1][x] > 0:
                        # connect topNode to n, make n a topNode
                        topNodes[x].addNeighbour(2, n)

                    # if node below, put n in topNodes
                    if data[y+1][x] > 0:
                        topNodes[x] = n
                    else:
                        topNodes[x] = None

        # find end node
        for i in range(1, width-1):
            if data[height-1][i] == 1:
                self.end = Maze.Node((height-1, i))
                self.nodeCount += 1
                # connects end node to the node above
                topNodes[i].addNeighbour(2, self.end)

    # convert 1d list to 2d-list using numpy
    def buildMatrix(self, width, height, data):
        newList = np.array(data).reshape(width, height)
        return newList
