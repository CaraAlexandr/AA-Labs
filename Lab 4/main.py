import time
import random
import matplotlib.pyplot as plt
import networkx as nx

# Implementation of DFS Algorithm in Python
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# Implementation of BFS Algorithm in Python
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# Create a graph with a given number of nodes and edges
def create_graph(num_nodes, num_edges):
    graph = {}
    for i in range(num_nodes):
        graph[i] = set()

    for i in range(num_edges):
        while True:
            node1 = random.randint(0, num_nodes - 1)
            node2 = random.randint(0, num_nodes - 1)
            if node1 != node2 and node2 not in graph[node1]:
                break
        graph[node1].add(node2)
        graph[node2].add(node1)
    return graph

# Test the DFS and BFS algorithms on a graph and record the execution time
def test_algorithm(graph):
    start_time = time.time()
    dfs_result = dfs(graph, 0)
    dfs_time = time.time() - start_time

    start_time = time.time()
    bfs_result = bfs(graph, 0)
    bfs_time = time.time() - start_time

    return len(graph), len(graph[0]), dfs_time, bfs_time

# Run the tests and record the results
graph_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
edge_densities = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
results = []
for size in graph_sizes:
    for density in edge_densities:
        num_edges = int(size * (size - 1) * density / 2)
        graph = create_graph(size, num_edges)
        results.append(test_algorithm(graph))

# Create graphs to visualize the results
fig, axs = plt.subplots(2, 2, figsize=(15, 15))
axs[0, 0].scatter([r[0] for r in results], [r[2] for r in results])
axs[0, 0].set_title('DFS Execution Time vs Graph Size')
axs[0, 0].set_xlabel('Number of Nodes')
axs[0, 0].set_ylabel('Execution Time (s)')
axs[0, 1].scatter([r[1] for r in results], [r[2] for r in results])
axs[0, 1].set_title('DFS Execution Time vs Node Degree')
axs[0, 1].set_xlabel('Average Node Degree')
axs[0, 1].set_ylabel('Execution Time (s)')
axs[1, 0].scatter([r[0] for r in results], [r[3] for r in results])
axs[1, 0].set_title('BFS Execution Time vs Graph Size')
axs[1, 0].set_xlabel('Number of Nodes')
axs[1, 0].set_ylabel('Execution Time (s)')
axs[1, 1].scatter([r[1] for r in results], [r[3] for r in results])
axs[1, 1].set_title('BFS Execution Time vs Node Degree')
axs[1, 1].set_xlabel('Average Node Degree')
axs[1, 1].set_ylabel('Execution Time (s)')
plt.show()

sample_graph = create_graph(10, 10)
nx.draw(nx.Graph(sample_graph), with_labels=True)
plt.show()