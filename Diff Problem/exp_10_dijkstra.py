#PRO 10
import heapq  # To use the priority queue (min-heap)

def dijkstra(graph, start, V):
    # Initialize distances and visited set
    distances = [float('inf')] * V
    distances[start] = 0  # Distance to the start node is 0
    visited = [False] * V  # Track visited nodes
    
    # Min-heap (priority queue), starting with the source node
    pq = [(0, start)]  # (distance, vertex)
    
    while pq:
        # Get the vertex with the smallest distance
        dist, u = heapq.heappop(pq)
        
        # If this node has already been processed, skip it
        if visited[u]:
            continue
        
        visited[u] = True  # Mark the node as visited
        
        # Update distances for adjacent vertices
        for v, weight in graph[u]:
            if not visited[v] and dist + weight < distances[v]:
                distances[v] = dist + weight
                heapq.heappush(pq, (distances[v], v))  # Push updated distance into the priority queue
    
    return distances

# Example usage:
# Graph representation using adjacency list (vertex -> [(neighbor, weight), ...])
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 5)],
    3: [(0, 6), (1, 8), (2, 5)]
}

V = 4  # Number of vertices
start = 0  # Starting vertex

shortest_paths = dijkstra(graph, start, V)
print("Shortest paths from vertex", start, ":", shortest_paths)
