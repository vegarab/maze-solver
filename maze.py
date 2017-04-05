
# MAZE-object representing the nodes in a graph,
# representing the paths in the maze
import numpy as np
class Maze:
    class Node:
        def __init__(self, position):
            self.position = position # position = (y,x)
            self.neighbours = [None, None, None, None] # left, top, right, bot

    def __init__(self, im):
        width, height = im.size
        data = list(im.getdata()) # list of pixels, 0 = black, 1 = white
        data = self.buildMatrix(width, height, data) # create a 2d array
        self.buildMaze(width, height, data) # create nodes and set start/end

    def buildMaze(self, width, height, data):

        # first and end-node
        self.start = None
        self.end = None

        # find start node
        for i in range(width):
            if (data[0][i] == 1):
                self.start = Maze.Node((0,i))

        # find end node
        for i in range(width):
            if(data[height-1][i] == 1):
                self.end = Maze.Node((height-1,i))

        # print out position of start and end node
        print(self.start.position)
        print(self.end.position)

        # left and top element relative to current node
        left = None
        top = None

        for y in range(1,height-2): # 1 and -2 to exclude last and first row
            for x in range(width-1):
                print()

        # TODO:
        # - Make sure to connect start and end node when maze is 'done'
        # - Delete the data-matrix from memory, but keep elements??


    # convert 1d list to 2d-list using numpy
    def buildMatrix(self, width, height, data):
        newList = np.array(data).reshape(width, height)
        return newList
