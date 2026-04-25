from collections import defaultdict

# Class to represent a directed graph
class Graph:
    def __init__(self, vertices):  # Correct constructor method
        self.graph = defaultdict(list)  # Adjacency list representation
        self.V = vertices  # Number of vertices

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Recursive helper function for topological sort
    def topological_sort_util(self, v, visited, stack):
        visited[v] = True  # Mark the current node as visited

        # Recur for all vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        stack.append(v)  # Push current vertex to stack which stores the result

    # The function to do Topological Sort
    def topological_sort(self):
        visited = [False] * self.V  # Mark all the vertices as not visited
        stack = []  # Stack to store the result in reverse order

        # Call the recursive helper function to store Topological Sort
        # starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        # Print contents of stack in reverse order to get topological order
        return stack[::-1]  # Reversed order gives the topological order

# Example usage
g = Graph(6)  # Create a graph with 6 vertices
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort of the given graph:")
print(g.topological_sort())
