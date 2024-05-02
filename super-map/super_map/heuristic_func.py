import math

def manhattan_distance(current, goal):
    dx = abs(current[0] - goal[0])
    dy = abs(current[1] - goal[1])
    return dx + dy

def diagonal_distance(current, goal):
    dx = abs(current[0] - goal[0])
    dy = abs(current[1] - goal[1])
    return max(dx, dy)  

def octile_distance(current, goal):
    dx = abs(current[0] - goal[0])
    dy = abs(current[1] - goal[1])
    return max(dx, dy) + (1.414 - 1) * min(dx, dy)  # 1.414 is sqrt(2)

def euclidean_distance(current, goal):
    dx = current[0] - goal[0]
    dy = current[1] - goal[1]
    return math.sqrt(dx * dx + dy * dy)