import heapq

# DFS algorithm for Adjacency Matrix
def dfs(adjacency_matrix, start, goal):
   visited = set()
   stack = [start]

   while stack:
       node = stack.pop()
       if node == goal:
           return True  # Path found (not necessarily shortest)

       if node not in visited:
           visited.add(node)
           neighbors = [i for i in range(len(adjacency_matrix)) if adjacency_matrix[node][i] > 0]
           stack.extend(neighbors)

   return False # No path found

# Dijkstra algorithm for Adjacency Matrix
def dijkstra(adjacency_matrix, start, goal):
    distances = [float('inf')] * len(adjacency_matrix)
    distances[start] = 0
    visited = set()

    heap = [(0, start)]  # (distance, node)

    while heap:
        cur_distance, cur_node = heapq.heappop(heap)
        
        if cur_node == goal:
            return cur_distance

        if cur_node not in visited:
            visited.add(cur_node)
            for neighbor, weight in enumerate(adjacency_matrix[cur_node]):
                if weight > 0:
                    new_distance = cur_distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(heap, (new_distance, neighbor))

    return -1  # No path found

# A* algorithm for Adjacency Matrix
def astar(adjacency_matrix, start, goal, heuristic):
    distances = [float('inf')] * len(adjacency_matrix)
    distances[start] = 0
    visited = set()

    heap = [(0, start)]  # (distance, node)

    while heap:
        cur_distance, cur_node = heapq.heappop(heap)
        
        if cur_node == goal:
            return cur_distance

        if cur_node not in visited:
            visited.add(cur_node)
            for neighbor, weight in enumerate(adjacency_matrix[cur_node]):
                if weight > 0:
                    new_distance = cur_distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(heap, (new_distance + heuristic[neighbor], neighbor))

    return -1  # No path found