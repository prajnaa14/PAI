#A_STAR
from collections import deque 
 
def heuristic(a, b): 
    (x1, y1) = a 
    (x2, y2) = b 
    return abs(x1 - x2) + abs(y1 - y2) 
 
def a_star_search(graph, start, goal): 
    frontier = deque([(start, [start], 0)]) 
    explored = set() 
     
    while frontier: 
        (node, path, cost) = frontier.popleft() 
         
        if node == goal: 
            return path 
         
        explored.add(node) 
         
        for neighbor in graph[node]: 
            if neighbor not in explored: 
                new_cost = cost + graph[node][neighbor] 
                frontier.append((neighbor, path + [neighbor], new_cost + heuristic(neighbor, goal))) 
         
        frontier = deque(sorted(frontier, key=lambda x: x[2])) 
     
    return [] 
 
# Example usage 
graph = { 
    (0, 0): {(0, 1): 1, (1, 0): 1}, 
    (0, 1): {(0, 0): 1, (0, 2): 1}, 
    (0, 2): {(0, 1): 1, (1, 2): 1}, 
    (1, 0): {(0, 0): 1, (2, 0): 1}, 
    (1, 2): {(0, 2): 1, (2, 2): 1}, 
    (2, 0): {(1, 0): 1, (2, 1): 1}, 
    (2, 1): {(2, 0): 1, (2, 2): 1}, 
    (2, 2): {(1, 2): 1, (2, 1): 1} 
} 
start = (0, 0) 
goal = (2, 2) 
path = a_star_search(graph, start, goal) 
print(path)
