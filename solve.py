# Main-file
# Solves the maze
from PIL import Image
import time
from maze import Maze

def solve(input_file):
    im = loadImage(input_file)
    data = list(im.getdata())

def loadImage(input_file):
    print ("Loading image ", input_file)
    im = Image.open(input_file)
    return im

def main():
    print("Hello World")
    input_file = input("File: ")
    solve(input_file)
    return 0

main()
