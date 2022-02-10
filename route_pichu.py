#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : Name: HIMANSHU HIMANSHU UserName: hhimansh
#
# Based on skeleton code provided in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col, visited_cells):
        
        # All moves which are possible along with their Direction
        moves=((row+1,col,'D'), (row-1,col,'U'), (row,col-1,'L'), (row,col+1,'R'))

        # Taken empty list to add valid moves
        valid_moves = []

        # Parsing to each possible move to check if it's valid
        for move in moves:
                        
                # Return only moves that are within the house_map and legal (i.e. go through open space ".") and also checked if we have traversed it or not
                if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@") and (visited_cells[move[0]][move[1]] == 0):
                        
                        # Marking the traversed position as 1 in the house_map and adding it to valid_moves list 
                        visited_cells[move[0]][move[1]] = 1
                        valid_moves.append(move)
        
        # Returning valid_moves list
        return valid_moves

# Calculating manhattan value for heuristic function
def calculate_manhattan_value(goal_row, goal_col, curr_row, curr_col):

        # Returning heuristic cost in manhattan value
        return abs(goal_row - curr_row) + abs(goal_col - curr_col)

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        
        # Find pichu goal position
        goal_loc = [(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="@"][0]
        
        # Map for marking the traversed cells
        visited_cells = [[0 for col in range(len(house_map[0]))] for row in range(len(house_map))]
        
        # Marking pichu start position as traversed
        visited_cells[pichu_loc[0]][pichu_loc[1]] = 1
        
        # Calculating starting position manhaton cost
        heuristic_value = calculate_manhattan_value(*goal_loc, *pichu_loc)
        
        # Calulating total cost for starting position(f(s) = c(s) + h(s))
        cost = 0 + heuristic_value
        
        # Implementing fringe in form of priority queue using dictionary of python (Setting cost as key and a list(all the coordinates with same cost) of tupples(coordination_location, distance to reach there, steps to reach there) as value)
        fringe ={cost:[(pichu_loc,0,'')]}
        
        # Iterating through Fringe till find a solution or Fringe is empty (No Solution Case)
        while fringe:

                # Making list of all priorities( heuristic costs) using dictionary keys method which give list of all keys
                heuristic_costs =  fringe.keys()

                # Use min method on list of priorities (heuristic cost) to find min priority (heuristic cost)
                min_heuristic_cost = min(heuristic_costs)
                
                # Retrieving the list of min priority (heuristic cost) coordinates
                min_heuristic_steps = fringe.pop(min_heuristic_cost)

                # Taking first element from min priority (heuristic cost) coordinate list
                (curr_move, curr_dist, curr_steps) = min_heuristic_steps[0] 

                # Slicing the min priority(heuristic cost) coordinate list
                min_heuristic_steps =  min_heuristic_steps[1:]

                # Checking if length of min priority list is not zero and if not zero setting it back to dictionary
                if len(min_heuristic_steps) != 0 :
                        fringe[min_heuristic_cost] = min_heuristic_steps
                
                # Calling moves function to get all the possible moves with their coordinates and step to do it
                for move in moves(house_map, *curr_move, visited_cells):
                        
                        # Checking if coordinates of next move is goal position
                        if house_map[move[0]][move[1]]=="@":
                                
                                # Returning the Solution with number of steps and steps to reach goal(adding 1 because it is next move, adding next move direction)
                                return (curr_dist + 1, curr_steps + move[2])

                        # Calculating cost(priority) for next step
                        cost = (curr_dist + 1) + calculate_manhattan_value(*goal_loc, move[0], move[1])
             
                        # Checking if cost(priority) exist in fringe
                        if cost in fringe:
                                
                                # If cost(priority) exist in the fringe appending new value(coordinates(row, col), distance to get there, steps to get there) to the already present list 
                                fringe[cost].append(((move[0], move[1]), curr_dist + 1, curr_steps + move[2]))
                                
                        else: 
                                # If cost(priority) is not present in the fringe we are adding new key cost(priority) and its value (coordinates(row, col), distance to get there, steps to get there) 
                                fringe[cost] = [((move[0], move[1]), curr_dist + 1, curr_steps + move[2])]

        # Returning the result if there is no solution
        return (-1, "")
# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1])

