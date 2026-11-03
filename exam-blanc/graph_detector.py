def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    current = set(graph)
    for _ in range(len(graph)):
        current = {nxt for node in current for nxt in graph.get(node, [])}
    return len(current) > 0

if __name__ == "__main__":
    print(py_graph_cycle_detector({0: [1], 1: [2], 2: [0]}))
    print(py_graph_cycle_detector({0: [1], 1: [2], 2: []}))
    print(py_graph_cycle_detector({}))
    print(py_graph_cycle_detector({0: [1, 2], 1: [3], 2: [3], 3: []}))
    print(py_graph_cycle_detector({0: [0]}))
    print(py_graph_cycle_detector({0: [1], 1: [2], 2: [3], 3: [1]}))
    print(py_graph_cycle_detector({0: [1], 1: [], 2: [3], 3: [2]}))
    print(py_graph_cycle_detector({0: [], 1: [], 2: []}))