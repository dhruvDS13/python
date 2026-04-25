#EXP 5
from collections import deque

# Class to represent a directed graph
class Graph:
    def __init__(self, vertices):  # Correct constructor method
        self.graph = {i: [] for i in range(vertices)}  # Initialize adjacency list

    def add_edge(self, u, v):
        self.graph[u].append(v)  # Add directed edge u -> v

    def bfs(self, start):
        visited = [False] * len(self.graph)  # Track visited nodes
        queue = deque([start])  # Start BFS from the start node
        visited[start] = True

        while queue:
            node = queue.popleft()
            print(node, end=" ")  # Process the current node

            # Visit all unvisited adjacent nodes
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    g = Graph(6)  # Graph with 6 vertices (0 to 5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    print("Nodes reachable from node 0:")
    g.bfs(0)
