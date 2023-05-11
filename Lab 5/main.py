import heapq
import random
import timeit
import networkx as nx
import matplotlib.pyplot as plt


def generate_random_graph(num_nodes, density):
    num_edges = int(density * num_nodes * (num_nodes - 1))
    graph = nx.gnp_random_graph(num_nodes, num_edges, directed=True)

    for (u, v, w) in graph.edges(data=True):
        w['weight'] = random.randint(0, 10)

    return nx.to_dict_of_dicts(graph)


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, data in graph[current_node].items():
            weight = data['weight']  # Extract the weight
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

def floyd_warshall(graph):
    nodes = list(graph.keys())

    # Initialize distances dictionary
    distances = {i: {j: float('infinity') for j in nodes} for i in nodes}
    for i in graph:
        for j in graph[i]:
            distances[i][j] = graph[i][j]['weight']

    for k in nodes:
        for i in nodes:
            for j in nodes:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances


def draw_graph(graph_dict, title):
    plt.title('Graph with this many nodes: ' + str(title))
    graph = nx.from_dict_of_dicts(graph_dict)  # Convert dict to NetworkX graph
    pos = nx.spring_layout(graph)  # Compute position of nodes for visualization
    nx.draw(graph, pos, with_labels=True)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)  # Add edge weights to visualization
    plt.show()


def analyze_algorithms():
    nodes_range = range(2, 52, 10)
    densities = [0.1, 0.9]  # Sparse and dense
    results = { 'dijkstra_sparse': [], 'dijkstra_dense': [], 'floyd_warshall_sparse': [], 'floyd_warshall_dense': [] }

    for num_nodes in nodes_range:
        for density in densities:
            graph = generate_random_graph(num_nodes, density)
            draw_graph(graph,num_nodes)

            start = timeit.default_timer()
            dijkstra(graph, 0)
            end = timeit.default_timer()

            if density == 0.1:
                results['dijkstra_sparse'].append(end - start)
            else:
                results['dijkstra_dense'].append(end - start)

            start = timeit.default_timer()
            floyd_warshall(graph)
            end = timeit.default_timer()

            if density == 0.1:
                results['floyd_warshall_sparse'].append(end - start)
            else:
                results['floyd_warshall_dense'].append(end - start)

    for algorithm, times in results.items():
        plt.plot(nodes_range, times, label=algorithm)

    plt.xlabel('Number of nodes')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    analyze_algorithms()
