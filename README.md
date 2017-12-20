# maze-solver
A few (simple) algorithms that solves image-formatted mazes

![maze image](/mazes/braid200-out.png)

## About

This is a personal project, based on Mike Pound's idea from Computerphile, that was meant to be a programming exercise.
Currently breadthfirst and depthfirst search has been implemented - change the import and method-calls from solve.py to
change between them. Other algorithms like Dijkstra or A-star might come in the future.

With a 2.6Ghz dual-core CPU and 16GB of RAM, the 10k x 10k maze with 1 unique solution is solved in ~300 seconds using breadthfirst search. 

## Note

There are some rules that the mazes needs to follow:
- Input images are .pngs that consists only of black and white pixels
- Black pixels are walls, white pixels are paths
- The maze is enclosed by walls
- The maze has 1 entrance at the top row and 1 exit at the bottom row

Some example inputs and outputs are in the /mazes folder. The mazes are generated using the software [Daedalus](http://www.astrolog.org/labyrnth/daedalus.htm).

The larger mazes require high amounts of RAM. Currently the 15k x 15k maze is unsolved with 16GB of available memory.

A few mazes are included in /mazes, as well as some output files marked \*-out.png

## Dependencies
 - Python3
 - Numpy
 - PIL (depreciated, but needed)

 Install with pip3: 
 ```
 pip3 install numpy
 pip3 install PIL  --allow-unverified PIL --allow-all-external
```

