
# MAZE-object representing the nodes in a graph,
# representing the paths in the maze
import numpy as np
class Maze:
    class Node:
        def __init__(self, position):
            self.position = position #position = (y,x)
            self.neighbours = [None, None, None, None] # left, top, right, bot

    def __init__(self, im):
        width, height = im.size
        data = list(im.getdata()) #list of pixels, 0 = black, 1 = white
    #    data = self.buildMatrix(width, height, data)
    #    x = self.buildMaze(width, height, data)

    def buildMaze(self, width, height, data):
        return 0
    # convert 1d list to 2d-list
    def buildMatrix(self, width, height, data):
        newList = np.array(data).reshape(width, height)
        return newList
