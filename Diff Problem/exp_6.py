#PROG 6

from collections import defaultdict

class Graph:
    def __init__(self, vertices):  # Correct constructor
        self.graph = defaultdict(list)  # Initialize adjacency list
        self.vertices = vertices  # Number of vertices in the graph

    def add_edge(self, u, v):
        self.graph[u].append(v)  # Add directed edge u -> v
        self.graph[v].append(u)  # For undirected graph, add reverse edge too

    def dfs(self, node, visited):
        visited[node] = True  # Mark the current node as visited
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def is_connected(self):
        visited = [False] * self.vertices  # Track visited nodes
        self.dfs(0, visited)  # Start DFS from node 0

        # Check if all vertices were visited
        return all(visited)

# Example usage
if __name__ == "__main__":
    g = Graph(5)  # Graph with 5 vertices (0 to 4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    # Note: Vertex 4 is not connected, so the graph is not connected.

    if g.is_connected():
        print("The graph is connected.")
    else:
        print("The graph is not connected.")
