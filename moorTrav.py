# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 00:28:12 2021

@author: SHULKA RAMLAL
Student Number: 219008485

"""

class Node:
    # Initialize the class
    def __init__(self, position:(), parent:()):
        self.position = position
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
 
    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
        
    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

    
def addOpen(open, neighbor):
    for node in open:
        if (neighbor == node):
            if(neighbor.f >= node.f):
                return False
    return True

    
def AStarAlgo(maze, start, end):
    openlist = []
    closed = []
    start_node = Node(start, None)
    goal_node = Node(end, None)
    openlist.append(start_node)
    

    while len(openlist) > 0:
        
        openlist.sort() 
        current_node = openlist.pop(0) 
        closed.append(current_node) 
        
        if current_node == goal_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            # Return reversed path
            return path[::-1]
        
        (x, y) = current_node.position
        
        neighbors = [(x, y+1), (x+1, y), (x-1, y+1), (x+1, y+1)]
        for next in neighbors:
            # Get value from map
            maze_value = maze[next[0]][next[1]]
            if(maze_value == 'W'):
                continue
            # Create a neighbor node
            neighbor = Node(next, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(neighbor.position[1] - start_node.position[1])   
            neighbor.f = neighbor.g + neighbor.h
            
            if(addOpen(openlist, neighbor) == True):
                openlist.append(neighbor)
    
    return None

def BestFirstAlgo(maze, start, end):
    openlist = []
    closed = []
    start_node = Node(start, None)
    goal_node = Node(end, None)
    openlist.append(start_node)
    

    while len(openlist) > 0:
        
        openlist.sort() 
        current_node = openlist.pop(0) 
        closed.append(current_node) 
        
        if current_node == goal_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            # Return reversed path
            return path[::-1]
        
        (x, y) = current_node.position
        
        neighbors = [(x, y+1), (x+1, y), (x-1, y+1), (x+1, y+1)]
        for next in neighbors:
            # Get value from map
            maze_value = maze[next[0]][next[1]]
            if(maze_value == 'W'):
                continue
            # Create a neighbor node
            neighbor = Node(next, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
            neighbor.f =  neighbor.h
            
            if(addOpen(openlist, neighbor) == True):
                openlist.append(neighbor)
    
    return None

def DFSAlgo(maze, start, end): 
    stackDFS, visitedNode = [start], set()
    frontier = []    
    while len(stackDFS) >= 1:
        if stackDFS[0] == start:
            path = [stackDFS.pop(0)]  
        else:
            path = stackDFS.pop(0)
            
        frontier = path[-1]
        if frontier == end:
            return path
        elif frontier not in visitedNode:
            for adjacentSpace in getAdjacentSpaces(maze, frontier, visitedNode):
                newPathToAppend = list(path)
                newPathToAppend.append(adjacentSpace)
                stackDFS.append(newPathToAppend)
            visitedNode.add(frontier)
    return None


def BFSAlgo(maze, start, end):   
    queueBFS, visitedNode = [start], set()
    frontier = []
    while len(queueBFS) >= 1:
        if queueBFS[0] == start:
            path = [queueBFS.pop(0)]  
        else:
            path = queueBFS.pop(0)
            
        frontier = path[-1]
        if frontier == end:
            return path
        elif frontier not in visitedNode:
            for adjacentSpace in getAdjacentSpaces(maze, frontier, visitedNode):
                newPathToAppend = list(path)
                newPathToAppend.append(adjacentSpace)
                queueBFS.append(newPathToAppend)
            visitedNode.add(frontier)
    return None


def getAdjacentSpaces(maze, space, visited):
     #Returns all legal action spaces 
    actionSpaces = list()
    finalAvailableSpaces = list()
    
    actionSpaces.append((space[0], space[1]+1))  # Right
    actionSpaces.append((space[0]-1, space[1] +1))  # Up & Right
    actionSpaces.append((space[0]+1, space[1] +1))  # Down & Right

    for i in actionSpaces:
        if maze[i[0]][i[1]] != 'W' and i not in visited: 
            finalAvailableSpaces.append(i)
    return finalAvailableSpaces


def printPathInMaze(maze, path):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if tuple([row, col]) in path:
                print("0", end="")
            else:
                print(maze[row][col], end="")
        print()
        

def readMazeFromFile(f):
    tempmaze = []
    varlist = []
    with open(f) as file:
        numRowsInMaze = int(file.readline().rstrip())
        numColumnsInMaze = int(file.readline().rstrip())
        for line in file:
            varlist = line.rstrip().split()
            for i in range(len(varlist)):
                if varlist[0] == 'D':
                    varlist[0]= 'S'
                if varlist[numColumnsInMaze-1] =='D':
                    varlist[numColumnsInMaze-1] = 'G'
            tempmaze.append(varlist)
    return tempmaze


def findStartOfMaze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if(maze[row][col] == 'S'):
                return tuple([row,col])
    return None


def findEndOfMaze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (maze[row][col] == 'G'):
                return tuple([row, col])
    return None

def main():
    
    fileName = input("Please enter the name of the file:")   
    
    if fileName.endswith(".txt"):
        file = fileName
    else:
        file = fileName+".txt"
    file = file.strip()
            
    try:
        print("valid document")
        maze = readMazeFromFile(file)
    except:
        print("No file detected, check if file is in folder")
        
    start = findStartOfMaze(maze) #Need to change end and start
    end = findEndOfMaze(maze)

    print("press 1 for Depth First Search")
    print("press 2 for Breadth First Search")
    print("press 3 for Best First Search")
    print("press 4 for A* Search")
    searchType  = input("enter a search: ")
    
    if searchType == "1":
        path = DFSAlgo(maze, start, end)
    elif searchType == "2":
        path = BFSAlgo(maze, start, end)
    elif searchType == "3":
        path = BestFirstAlgo(maze, start, end)
    elif searchType == "4":
        path = AStarAlgo(maze, start, end)
    else:
        print("Invalid input, sealect a number from 1 - 4")
    
        
    if path == None:
        """
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if maze[row][col]== 'S':
                    maze[row][col]= 'W'
                    break
        wChangeCounter = 0
        rowCounter = 0
        for row1 in range(len(maze)):
            rowCounter = rowCounter +1
            for col in range(len(maze[0])):
                if maze[row1][0] == 'W':
                    wChangeCounter = wChangeCounter+1
                        
        if wChangeCounter == rowCounter:
            print("No solution after entering each start")
        else:
            start = findStartOfMaze(maze)
            if searchType == "1":
                path = DFSAlgo(maze, start, end)
            elif searchType == "2":
                path = BFSAlgo(maze, start, end)
            elif searchType == "3":
                path = BestFirstAlgo(maze, start, end)
            else:
                path = AStarAlgo(maze, start, end)
        """
        print("no solution")
    
    else:
        printPathInMaze(maze, path)
        print("")
        print("Path to a goal state is: ")
        print(path)
        
    name = input("Press enter to exit")




if __name__ == "__main__":
    main()

