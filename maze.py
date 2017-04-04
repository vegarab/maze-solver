
# MAZE-object representing the nodes in a graph,
# representing the paths in the maze
class Maze:
    class Node:
        def __init__(self, position):
            self.position = position #position = (y,x)
            self.neighbours = [None, None, None, None] # left, top, right, bot

    def __init__(self, im):

        width, height = im.size
        data = list(im.getdata()) #list of pixels, 0 = black, 1 = white
        x = self.buildMaze(width, height, data)

    def buildMaze(self, width, height, data):
        print "hello"
        return 0
