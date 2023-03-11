from queue import Queue

class Graph:
    """
    Реализация графа использую список смежности
    """
    def __init__(self, num_of_nodes, directed=True) -> None:
        self.num_of_nodes = num_of_nodes
        self.nodes = range(self.num_of_nodes)
        self.directed = directed
        self.adj_list_edges = {node: set() for node in self.nodes}

    def add_edge(self, node1, node2, weight=1) -> None:
        self.adj_list_edges[node1].add((node2, weight))

        if not self.directed:
            self.adj_list_edges[node2].add((node1, weight))

    def print_adj_list_nodes(self) -> None:
        for key in self.adj_list_edges.keys():
            print(f'Node {key} : {self.adj_list_edges[key]}')

    def dfs(self, start, target, path = [], visited = set()):
        """
        Алгоритм поиска в глубину
        """
        path.append(start)
        visited.add(start)
        if start == target:
            return path
        # проход по соседним узлам начального
        for (neighbour, weight) in self.adj_list_edges[start]:
            if neighbour not in visited:
                result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None
    
    def bfs(self, start_node, target_node):
        """
        Алгоритм поиска в ширину
        """
        visited = set()
        queue = Queue()

        queue.put(start_node)
        visited.add(start_node)

        # стартовая вершина не имеет родителей
        parent = dict()
        parent[start_node] = None

        path_found = False

        while not queue.empty():
            current_node = queue.get()
            if current_node == target_node:
                path_found = True
                break

            for (next_node, weight) in self.adj_list_edges[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    parent[next_node] = current_node
                    visited.add(next_node)

        # получение пути
        path = []
        if path_found:
            path.append(target_node)
            while parent[target_node] is not None:
                path.append(parent[target_node])
                target_node = parent[target_node]
            path.reverse()

        return path

# орентированный граф
# для создания неорентированного графа, добавить directed=False
graph = Graph(5, directed=False)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_adj_list_nodes()

traversal_path = []
traversal_path = graph.dfs(0, 3)
print(traversal_path)

graph_ = Graph(6, directed=False)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 5)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 5)

graph.print_adj_list()

path = []
path = graph.bfs(0, 5)
print(path)