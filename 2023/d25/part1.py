import argparse
import networkx as nx


def calculate(data):
    graph = nx.Graph()

    for line in data:
        root, nodes = line.split(":")
        for node in nodes.strip().split():
            graph.add_edge(root, node)
            graph.add_edge(node, root)

    graph.remove_edges_from(nx.minimum_edge_cut(graph))
    x, y = nx.connected_components(graph)

    return len(x) * len(y)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true", help="Run with the test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
""".strip().split("\n")

    if not args.test:
        with open(args.input, 'r') as file:
            file_data = file.read()
        test_data = file_data.strip().split('\n')

    print("Answer:", calculate(test_data))
