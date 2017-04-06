# Main-file
# Solves the maze
from PIL import Image
import time
from maze import Maze

def solve(input_file):
    print ("Loading image ", input_file)
    im = loadImage(input_file)

    print ("Building maze")
    t0 = time.time()
    maze = Maze(im)
    t1 = time.time()
    print ("Node count: ", maze.nodeCount)
    total = t1-t0
    print ("Time elapsed: ", total, "\n")

def loadImage(input_file):
    return Image.open(input_file)

def main():
    input_file = input("File: ")
    solve("/home/vegarab/python/maze-solver/mazes/"+input_file)
    return 0

main()
