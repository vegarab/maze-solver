# Main-file
# Solves the maze

from PIL import Image
import time
import breadthfirst
import breadthfirst1
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
    [result, stats] = breadthfirst1.solve(maze)

    #for i in range(0,len(result)):
    #    print (result[i].position)

    t1 = time.time()
    total = t1-t0

    print ("Visited ", stats[0], " node(s)")
    print ("Path length: ", stats[1])
    print ("Time elapsed: ", total)

    # Draws the output image
    # Draws the path from beginning to end in red
    """
    print ("Saving output-image")
    im = im.convert("RGB")
    impixels = im.load()

    resultpath = [n.position for n in result]
    px = (255,0,0) # Red

    #print(resultpath)

    for i in range(0, len(resultpath)-1):

        a = resultpath[i]
        b = resultpath[i+1]

        #print(i)
        #print("a0, b0: ", a, " ", b)
        if (a[0] == b[0]):
            # Ys are equal, horizontal line
            for x in range(min(a[1], b[1]), max(a[1], b[1])):
                impixels[x, a[0]] = px
        elif (a[1] == b[1]):
            # Xs are equal, vertical line
            for y in range(min(a[0], b[0]), max(a[0], b[0]+1)):
                impixels[a[1], y] = px

    im.save(output_file)
    """
    print ("Saving Image")
    im = im.convert('RGB')
    impixels = im.load()

    resultpath = [n.position for n in result]

    length = len(resultpath)

    for i in range(0, length - 1):
        a = resultpath[i]
        b = resultpath[i+1]

        # Blue - red
        r = int((i / length) * 255)
        px = (r, 0, 255 - r)

        if a[0] == b[0]:
            # Ys equal - horizontal line
            for x in range(min(a[1],b[1]), max(a[1],b[1])):
                impixels[x,a[0]] = px
        elif a[1] == b[1]:
            # Xs equal - vertical line
            for y in range(min(a[0],b[0]), max(a[0],b[0]) + 1):
                impixels[a[1],y] = px

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
