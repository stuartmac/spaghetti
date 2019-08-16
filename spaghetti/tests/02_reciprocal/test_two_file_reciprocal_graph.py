import unittest

import networkx as nx

from spaghetti import Spaghetti


class TwoFileGraphTestCase(unittest.TestCase):
    def test_two_file_graph(self):
        # example files should resolve to foo.txt <-> bar.txt
        expected_graph = nx.DiGraph()
        expected_graph.add_nodes_from(['foo.txt', 'bar.txt'])
        expected_graph.add_edges_from([('foo.txt', 'bar.txt'), ('bar.txt', 'foo.txt')])

        # calculate graph using spaghetti
        calculated_graph = Spaghetti(['foo.txt', 'bar.txt']).graph

        # convert to comparable format and test they're the same
        expected_adjacency = list(expected_graph.adjacency())
        calculated_adjacency = list(calculated_graph.adjacency())
        self.assertCountEqual(expected_adjacency, calculated_adjacency)


if __name__ == '__main__':
    unittest.main()
