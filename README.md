# AI-maze-search-

The heuristic evaluation function used for the A* algorithm
The heuristic function for the A* star algorithm is f = h + g where h is the
estimated distance from the current node to the goal node and g is the calculated
distance from the start node to the current node. There are many ways of
calculating your distance, some of the ways is taking the Euclidian distance of the
two points, another method is calculating the Manhattan distance. In this
assignment, the Manhattan heuristic is used. This is because it always yields a
positive number and a whole number, making it easier to evaluate the heuristics of
the nodes. The Manhattan heuristic is calculated by taking the absolute value of the
neighboring node’s row position subtracted by the goal/start node’s row position
added to the neighboring node’s column position subtracted by the goal/start
node’s column position. 

A comparison of performance of the four search algorithms
In the given assignment, the maze had to be solved using four types of algorithms.
Namely: the Depth First Search, Breadth First Search, Best First Search and the
A* Search.
Depth First Search: For depth first search, the algorithm explores the lower levels
of the maze first. The beast case time complexity for DFS is O(1). With that noted,
the beast place to use depth first search is in problems that have one solution. Since
a 2D array is used to store the maze, and the time complexity of DFS is dependent
on the data structure used, the time complexity for this maze problem would be
O(bᵐ) with b being the branching factor and m being the depth. The space
complexity is O(bm). Depth first search is not optimal nor is it complete.
Breadth First Search: Breadth first search evaluates all nodes at the same level
before moving on to the next lower level. The time and space complexity for
breadth first search is O(bᵈ) with b being the branching factor and d being the
depth of the shallowest solution. The best case complexity would be O(1). Breadth first search is optimal as long as the cost of all the edges are the same.
It is also complete.
Best First Search: The best first search expands the nodes with the smallest
heuristic value (in this case f = h). This algorithm makes an intelligent guess that
selecting nodes closer to the goal may yield a faster result. The beast case time
complexity is O(bm) with b being the branching factor and m being the depth
whilst the worst case is O(|V|) I which V is the number of nodes. Best first search
is complete and if the heuristic is admissible, is may be optimal.
A* Search: A* search is best first search with a different heuristic function. In A*
search f = h + g. The A* search takes in account the approximate total distance
needed to travel to the goal node and expands the best next node. The time
complexity for A* search is O(bd) where b is the branching factor and d is the
depth of the shortest solution. If the heuristic is admissible, then this algorithm is
optimal and complete.
By comparing the above information of the four searches, it is easy to see that if
the heuristic is admissible, the best search for a larger maze would be A* since it
takes in the overall distance in the heuristic when selecting the next node. The next
best search for larger mazes would be Best First. This search is also dependent on
the admissibility of the heuristic function. The next best would be Depth First
search for a larger maze, if the maze is smaller then Breadth First search may be
better. 
