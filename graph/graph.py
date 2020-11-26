from collections import defaultdict
from typing import DefaultDict, List, KeysView


class Graph(object):

    def __init__(self):
        self.adjacencies: DefaultDict[str, List[str]] = defaultdict(list)

    def add_edge(self, vertex_from: str, vertex_to: str):
        self.adjacencies[vertex_from].append(vertex_to)

    def get_vertices_with_edge(self) -> KeysView[str]:
        return self.adjacencies.keys()

    def find_longest_path_from(self, vertex_from: str) -> int:
        if vertex_from not in self.get_vertices_with_edge():
            raise ValueError("Vertex does not have edges or does not exist")
        return self.dfs(vertex_from, 1)

    def dfs(self, start_node: str, current_path: int) -> int:
        result_path = current_path
        if start_node not in self.get_vertices_with_edge():
            return result_path
        for edge in self.adjacencies[start_node]:
            result_path = max(result_path, self.dfs(edge, current_path + 1))  # реалізація під капотом?
        return result_path
