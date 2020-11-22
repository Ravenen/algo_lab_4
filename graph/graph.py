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
        return self.dfs(vertex_from, 1)

    def dfs(self, start_node: str, current_path: int) -> int:
        result_path = current_path
        if start_node not in self.adjacencies.keys():
            return result_path
        for edge in self.adjacencies[start_node]:
            result_path = max(result_path, self.dfs(edge, current_path + 1))
        return result_path
