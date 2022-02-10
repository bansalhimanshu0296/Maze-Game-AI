# Maze-Game-AI #

This project was done as a part of CSCI-B-551 Elements of Artificial Intelligence Coursework under Prof. Dr. David Crandall.

## Command to run the program ##

python3 route_pichu.sh [name of map]

## Abstractions Techniques that can be used ##

Another Abstraction technique I would have used could be the Breadth-First Search. But the problem with the Breadth-First Search is not an optimal algorithm for a maze solver problem, which means sometimes it does not give the optimal path.

## Abstraction Technique Used ##

I am using the A* search technique for implementation which is complete and optimal in the case of the Maze Solver Problem.

## Overview of Solution ##

I have chosen the A* search technique for implementation which is complete and optimal in the case of the Maze Solver Problem. For implementing A* Search we need a heuristic function. So, I have chosen the Manhattan value which is admissible and consistent for 4 directions to calculate the heuristic value. Another reason for choosing the Manhattan value was we can only move in cells and not in a straight line from start to goal location. Manhattan value can be calculated by using x-y coordinates abs(x2-x1) + abs(y2-y1).

So, in the actual solution firstly I have found the initial pichu's location and goal locations. I changed the fringe structure. I used the dictionary for implementing fringe like a priority queue. I take the priority which is the heuristic cost of coordinate as the key of dictionary and value as a list of tuples. This tuple contains the coordinates of the location, the number of moves to reach that location, and steps(direction) to reach the location. The main reason to choose a dictionary was that it's easy to retrieve data from the dictionary and it is also easy to get keys that are heuristic cost using inbuilt python functions. Initially added the starting pichu_loc, 0, and "" as tuple to the fringe with its heuristic cost as key. After that, I ran a loop until the fringe is empty(which was already implemented in the stub) which is the case when there is no solution for the problem. In the loop firstly I make a list of all the priorities(heuristic cost) in the heuristic_costs variable after that I am finding the minimum heuristic cost out of that using the min function on the list of heuristic costs(heuristic_costs). After that, I am retrieving the list of tuples from the dictionary for the minimum heuristic cost and taking the one element from the list, and set the rest of the elements if there is any left for the minimum heuristic cost to the dictionary. Then calling the moves function on derived coordinate to get all the moves that are possible for coordinate. Made a change to moves function added direction to the tuple i.e.(U, D, L, R) according to coordinates to get the direction of it and moves function is returning moves which are valid depending on two conditions which are it should be an empty space, not a wall and should be in the map. Then I am returning the moves and running a loop on each move to check if it is the goal location if it is then return the number of steps to get there by adding one to the previous number of moves and steps to get there by adding appending this move direction to already existing moves for the previous step. Otherwise calculated the heuristic cost for the move and checked if that heuristic cost already exists in the fringe, if it is there appending the new move to already existing list of heuristic cist otherwise add a new key i.e. heuristic cost of coordinate, value (tuple of the coordinate, number of steps, steps) pair in the dictionary. At last, if the fringe becomes empty i.e. loops end I am returning -1 and empty string as result.

## Challenges Faced and Solution for it ##

When I implemented the above solution I came across a challenge of the infinite loop if there was no solution for the map which can be a problem in the A* abstraction technique. So, to overcome that challenge I have created a traversed cells map which is a nested list of the same dimensions as an input map that is storing data in form of binary 0 or 1. 0 for not traversed node and 1 for traversed node. I have initialized this map in search function with all 0 and then I have set it 1 for start location. It also changed my moves function I am passing my traversed cell map to the function and added a new valid condition for checking if the coordinate is valid or not. The new condition was if the coordinate is already traversed meaning it has been added in the fringe or not if it has been then the coordinate is not a valid one. If it's a valid move I am updating my traversed cell map and setting the cell from 0 to 1 and returning the move from the solve function.

## Initial State ##

The initial state for the solution is the map with the pichu placed at starting position.

## Goal State ##

The goal state for the solution is pichu reaches the coordinates where @ is present.

## Cost Function ##

The cost function which I used for the solution is the heuristic cost function and to calculate that I have used the manhattan value which can be found in the calculate_manhattan_value function of the program.

## State Space ##

State-space for the solution is every coordinate where pichu can go from initial state or initial state where pichu is present represented by p in the initial map and the goal state where pichu has to reach represented by @

## Succesor Function ##

The successor function in this solution gives every next possible move according to the current position of pichu.



