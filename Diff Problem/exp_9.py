#PROG 9
import heapq  # To use a priority queue (min-heap)

def prim_mst(graph, V):
    # Initialize a min-heap for edges
    min_heap = []
    heapq.heappush(min_heap, (0, 0))  # Start with node 0, cost 0
    visited = [False] * V  # Track visited nodes
    total_cost = 0  # To store the total cost of MST
    mst_edges = []  # To store the edges in the MST

    while min_heap:
        cost, u = heapq.heappop(min_heap)  # Get the vertex with the minimum edge cost
        if visited[u]:
            continue  # Skip if the vertex is already visited
        visited[u] = True  # Mark the vertex as visited
        total_cost += cost  # Add the cost to the MST total cost

        # Add the edge to the MST (skip the first edge as its cost is 0)
        if cost > 0:
            mst_edges.append((prev_node, u, cost))  # Add the edge (previous node, current node, cost)

        # Add all adjacent edges to the heap
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))
                prev_node = u  # Track the previous node to form edges

    return total_cost, mst_edges

# Example usage:
# Graph representation using adjacency list (vertex -> [(neighbor, weight), ...])
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 5)],
    3: [(0, 6), (1, 8), (2, 5)]
}

V = 4  # Number of vertices
cost, mst = prim_mst(graph, V)
print("Total cost of MST:", cost)
print("Edges in MST:", mst)
