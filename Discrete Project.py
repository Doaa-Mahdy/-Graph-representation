import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Function to convert adjacency list to adjacency matrix


def adjacency_list_to_matrix(adj_list):
    num_vertices = len(adj_list)
    adjacency_matrix = np.zeros((num_vertices, num_vertices), dtype=int)

    for vertex, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            adjacency_matrix[vertex][neighbor] = 1

    return adjacency_matrix

# Function to draw the graph


def draw_graph(adj_list):
    graph = nx.Graph()
    for vertex, neighbors in enumerate(adj_list):
        graph.add_edges_from((vertex, neighbor) for neighbor in neighbors)

    nx.draw(graph, with_labels=True)
    plt.show()

# Function to count the paths between vertices using DFS


def count_paths(adj_list, start_vertex, end_vertex):
    count = 0
    visited = set()

    def dfs(current_vertex):
        nonlocal count
        visited.add(current_vertex)

        if current_vertex == end_vertex:
            count += 1
        else:
            for neighbor in adj_list[current_vertex]:
                if neighbor not in visited:
                    dfs(neighbor)

        visited.remove(current_vertex)

    dfs(start_vertex)
    return count

# Example usage


print("Sample input: [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]")
adj_list = []
num_vertices = int(input("Enter the number of vertices in the graph: "))
for i in range(num_vertices):
    neighbors = input(
        "Enter the neighbors of vertex {} (space-separated): ".format(i)).split()
    adj_list.append([int(neighbor) for neighbor in neighbors])

adjacency_matrix = adjacency_list_to_matrix(adj_list)

print("Adjacency Matrices:")
print(adjacency_matrix)


start_vertex = int(input("Enter the start vertex: "))
end_vertex = int(input("Enter the end vertex: "))

path_count = count_paths(adj_list, start_vertex, end_vertex)

print("Number of paths between", start_vertex,
      "and", end_vertex, ":", path_count)

draw_graph(adj_list)

