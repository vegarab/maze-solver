# Main-file
# Solves the maze

from PIL import Image
import time
import breadthfirst
import depthfirst
from maze import Maze

def solve(input_file, output_file):
    print ("Loading image ", input_file, "\n")
    im = loadImage(input_file)

    print ("Building maze")
    t0 = time.time()
    maze = Maze(im)

    t1 = time.time()
    print ("Node count: ", maze.nodeCount)
    total = t1-t0
    print ("Time elapsed: ", total, "\n")

    print ("Starting breadthfirst solve.")
    t0 = time.time()
    [result, stats] = breadthfirst.solve(maze)

    t1 = time.time()
    total = t1-t0

    print ("Visited ", stats[0], " node(s)")
    print ("Path length: ", stats[1])
    print ("Time elapsed: ", total)

    # Draws the output image
    # Draws the path from beginning to end in red
    print ("Saving output-image")
    im = im.convert("RGB")
    impixels = im.load()

    resultpath = [n.position for n in result]
    px = (255,0,0) # Red

    for i in range(0, len(resultpath)-1):

        a = resultpath[i]
        b = resultpath[i+1]

        if (a[0] == b[0]):
            # Ys are equal, horizontal line
            if a[1] > b[1]:
                for x in range(b[1], a[1]+1):
                    impixels[x, a[0]] = px
            elif a[1] < b[1]:
                for x in range(a[1], b[1]):
                    impixels[x, a[0]] = px
        elif (a[1] == b[1]):
            # Xs are equal, vertical line
            if a[0] < b[0]:
                for y in range(a[0], b[0]+1):
                    impixels[a[1], y] = px
            elif a[0] > b[0]:
                for y in range(a[0], b[0], -1):
                    impixels[a[1], y] = px

    im.save(output_file)
    print ("Complete!")

def loadImage(input_file):
    return Image.open(input_file)

def main():
    file_path = "/home/vegarab/python/maze-solver/mazes/"
    input_file = input("File: ")
    output_file = input("Output file: ")
    solve(file_path+input_file, file_path+output_file)

    return 0

main()
