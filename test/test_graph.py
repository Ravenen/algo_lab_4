from unittest import TestCase

from graph.graph import Graph


class TestGraph(TestCase):

    def setUp(self) -> None:
        self.first_one_edge_graph = Graph()
        self.first_one_edge_graph.add_edge("1", "2")

        self.second_multi_edge_graph = Graph()
        self.second_multi_edge_graph.add_edge("1", "2")
        self.second_multi_edge_graph.add_edge("1", "3")
        self.second_multi_edge_graph.add_edge("3", "4")
        self.second_multi_edge_graph.add_edge("4", "5")
        self.second_multi_edge_graph.add_edge("2", "6")
        self.second_multi_edge_graph.add_edge("6", "4")

    def test_add_edge_first_quantity(self):
        self.assertEqual(1, len(self.first_one_edge_graph.adjacencies.keys()))

    def test_add_edge_first_composition(self):
        self.assertSetEqual({"1"}, set(self.first_one_edge_graph.adjacencies.keys()))

    def test_get_vertices_with_edge_first_quantity(self):
        self.assertEqual(1, len(self.first_one_edge_graph.get_vertices_with_edge()))

    def test_get_vertices_with_edge_first_composition(self):
        self.assertSetEqual({"1"}, set(self.first_one_edge_graph.get_vertices_with_edge()))

    def test_find_longest_path_from_first_normal(self):
        self.assertEqual(2, self.first_one_edge_graph.find_longest_path_from("1"))

    def test_find_longest_path_from_first_invalid(self):
        with self.assertRaises(ValueError):
            self.first_one_edge_graph.find_longest_path_from("2")
        with self.assertRaises(ValueError):
            self.first_one_edge_graph.find_longest_path_from("5")

    def test_add_edge_second_quantity(self):
        self.assertEqual(5, len(self.second_multi_edge_graph.adjacencies.keys()))

    def test_add_edge_second_composition(self):
        self.assertSetEqual({"1", "2", "3", "4", "6"}, set(self.second_multi_edge_graph.adjacencies.keys()))

    def test_get_vertices_with_edge_second_quantity(self):
        self.assertEqual(5, len(self.second_multi_edge_graph.get_vertices_with_edge()))

    def test_get_vertices_with_edge_second_composition(self):
        self.assertSetEqual({"1", "2", "3", "4", "6"}, set(self.second_multi_edge_graph.get_vertices_with_edge()))

    def test_find_longest_path_from_second_normal(self):
        self.assertEqual(5, self.second_multi_edge_graph.find_longest_path_from("1"))
        self.assertEqual(3, self.second_multi_edge_graph.find_longest_path_from("6"))
        self.assertEqual(2, self.second_multi_edge_graph.find_longest_path_from("4"))

    def test_find_longest_path_from_second_invalid(self):
        with self.assertRaises(ValueError):
            self.second_multi_edge_graph.find_longest_path_from("5")

