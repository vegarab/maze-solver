# Main-file
# Solves the maze
from PIL import Image
import time
from maze import Maze

def solve(input_file):
    im = loadImage(input_file)
    maze = Maze(im)

def loadImage(input_file):
    print ("Loading image ", input_file)
    im = Image.open(input_file)
    return im

def main():
    print("Hello World")
    input_file = input("File: ")
    solve("/home/vegarab/python/maze-solver/mazes/"+input_file)
    return 0

main()
