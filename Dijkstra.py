import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.graph:
            self.add_node(from_node)
        if to_node not in self.graph:
            self.add_node(to_node)
        self.graph[from_node].append((to_node, weight))


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph.graph}
    distances[start] = 0
    predecessors = {node: None for node in graph.graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    path = path[::-1]

    if distances[end] == float('inf'):
        return None, None
    return distances[end], path


if __name__ == "__main__":
    graph = Graph()

    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 6)
    graph.add_edge('C', 'D', 3)
    graph.add_edge('C', 'E', 1)
    graph.add_edge('D', 'E', 2)

    start_node = 'A'
    end_node = 'E'
    distance, path = dijkstra(graph, start_node, end_node)

    if distance is not None:
        print(f"Najkrótsza odległość z {start_node} do {end_node} to {distance}")
        print(f"Ścieżka: {' -> '.join(path)}")
    else:
        print(f"Nie ma ścieżki z {start_node} do {end_node}")
