import unittest

from stratego.Stratego import Stratego


class TestStratego(unittest.TestCase):
    def test_edges(self):
        stratego = Stratego(4)

        edges = [
            # rows
            [(0, 0), (1, 0), (2, 0), (3, 0)],
            [(0, 1), (1, 1), (2, 1), (3, 1)],
            [(0, 2), (1, 2), (2, 2), (3, 2)],
            [(0, 3), (1, 3), (2, 3), (3, 3)],
            # columns
            [(0, 0), (0, 1), (0, 2), (0, 3)],
            [(1, 0), (1, 1), (1, 2), (1, 3)],
            [(2, 0), (2, 1), (2, 2), (2, 3)],
            [(3, 0), (3, 1), (3, 2), (3, 3)],
            # diagonals
            [(0, 0), (1, 1), (2, 2), (3, 3)],
            [(1, 0), (2, 1), (3, 2)],
            [(1, 0), (0, 1)],
            [(2, 0), (3, 1)],
            [(2, 0), (1, 1), (0, 2)],
            [(3, 0), (2, 1), (1, 2), (0, 3)],
            [(1, 3), (2, 2), (3, 1)],
            [(1, 3), (0, 2)],
            [(2, 3), (3, 2)],
            [(2, 3), (1, 2), (0, 1)]
        ]

        sorted_edges = sorted([sorted(edge) for edge in edges])

        self.assertEqual(len(edges), len(stratego.edges))
        self.assertEqual(sorted_edges, sorted(stratego.edges))


if __name__ == '__main__':
    unittest.main()
