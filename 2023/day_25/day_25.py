import networkx as nx


def part1(in_text):
    edges = []
    for line in in_text.split('\n'):
        node1, connected = line.split(': ')
        for node2 in connected.split():
            edges.append((node1, node2))

    graph = nx.from_edgelist(edges)
    edge_betweenness = nx.edge_betweenness_centrality(graph)
    most_crucial_edges = sorted(edge_betweenness, key=edge_betweenness.get)[-3:]
    graph.remove_edges_from(most_crucial_edges)
    size1, size2 = [len(c) for c in nx.connected_components(graph)]
    return size1 * size2


puzzle_input = open('input.txt').read()
print(part1(puzzle_input))
