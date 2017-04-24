# maze-solver
A few algorithms that solves image-formatted mazes

## About

This is a personal project, based on Mike Pound's idea from Computerphile, that was meant to be a programming exercise.
Currently breadthfirst and depthfirst search has been implemented - change the import and method-calls from solve.py to
change between them. Other algorithms like Dijkstra or A-star might come in the future.

## Note

There are some rules that the mazes needs to follow:
- Input images are .pngs that consists only of black and white pixels
- Black pixels are walls, white pixels are paths
- The maze is enclosed by walls
- The maze has 1 entrance at the top row and 1 exit at the bottom row

Some example inputs and outputs are in the /mazes folder. The mazes are generated using the software [Daedalus](http://www.astrolog.org/labyrnth/daedalus.htm).

The larger mazes require high amounts of RAM. Currently the 15kx15k maze is unsolved with 16GB of available memory. 
