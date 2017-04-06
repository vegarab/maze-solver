
# MAZE-object representing the nodes in a graph,
# representing the paths in the maze
import numpy as np
class Maze:
    class Node:
        def __init__(self, position):
            self.position = position # position = (y,x)
            self.neighbours = [None, None, None, None] # left, right, top, bot

        def addNeighbour(self, pos, node):
            # left
            if (pos == 0):
                self.neighbours[0] = node
                node.neightbours[1] = self
            # right
            elif (pos == 1):
                self.neighbours[1] = node
                node.neighbours[0] = self
            # top
            elif (pos == 2):
                self.neighbours[2] = node
                node.neighbours[3] = self
            # bot
            elif (pos == 3):
                self.neighbours[3] = node
                node.neighbours[2] = self

    def __init__(self, im):
        width, height = im.size
        data = list(im.getdata()) # list of pixels, 0 = black, 1 = white
        data = self.buildMatrix(width, height, data) # create a 2d array
        self.buildMaze(width, height, data) # create nodes and set start/end

    def buildMaze(self, width, height, data):

        # first and end-node
        self.start = None
        self.end = None

        # nodes above current row
        topNodes = [] * width

        # find start node
        for i in range(1, width-1):
            if (data[0][i] == 1):
                self.start = Maze.Node((0,i))
                topNodes[i] = self.start # add start node to topNodes at pos
                break

        # find end node
        for i in range(width):
            if(data[height-1][i] == 1):
                self.end = Maze.Node((height-1,i))

        # print out position of start and end node
        print(self.start.position)
        print(self.end.position)

        for y in range(1,height-2): # 1 and -2 to exclude last and first row
            # new node
            n = None
            # node left of current
            leftNode = None

            for x in range(1,width-1): # 1 to exclude left wall and NullPointer

                # if on wall, do nothing
                if data[y][x] > 0:
                    continue

                # PATH PATH PATH
                if (data[y][x-1] > 0 and data[y][x+1] > 0):
                    # create node if path above
                    n.Maze.Node((y,x))
                    leftNode.addNeighbour(1,n)
                    leftNode = n

                # WALL PATH PATH
                # create node if start of corridor

                # PATH PATH WALL
                # create node if end of corridor

                # WALL PATH WALL
                # create nod if dead end

                # check topNodes

        # TODO:
        # - Make sure to connect start and end node when maze is 'done'
        # - Delete the data-matrix from memory, but keep elements??


    # convert 1d list to 2d-list using numpy
    def buildMatrix(self, width, height, data):
        newList = np.array(data).reshape(width, height)
        return newList
