from unittest import TestCase

from app import is_one_letter_differ, fill_in_graph_with_words, sort_words_by_length_descending
from graph.graph import Graph


class Test(TestCase):
    def test_is_one_letter_differ(self):
        self.assertTrue(is_one_letter_differ("PythonTest", "PytonTest"))
        self.assertFalse(is_one_letter_differ("Hello", "Heo"))
        self.assertTrue(is_one_letter_differ("A", ""))

    def test_fill_in_graph_with_words(self):
        graph = Graph()
        graph = fill_in_graph_with_words(graph, ["ratata", "ratta", "atata", "ratt", "att", "a"])
        self.assertEqual(3, len(graph.get_vertices_with_edge()))
        self.assertSetEqual({"ratata", "ratta", "ratt"}, set(graph.get_vertices_with_edge()))

    def test_sort_words_by_length_descending(self):
        self.assertListEqual(["123456", "123", "12", "1"],
                             sort_words_by_length_descending(["1", "123", "123456", "12"]))
        self.assertListEqual(["1"],
                             sort_words_by_length_descending(["1"]))
