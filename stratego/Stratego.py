from copy import deepcopy


class Stratego:
    size = 4

    def __init__(self, size):
        self.size = size
        self.placed = []
        self.available = []
        self.edges = []

        r = range(size)

        for i in r:
            for j in r:
                new = (i, j)
                if new not in self.available:
                    self.available.append(new)

        self.generate_edges(size)

    def add_edge(self, edge):
        if len(edge) > 1:
            sorted_edge = sorted(edge)

            if sorted_edge not in self.edges:
                self.edges.append(sorted_edge)

    def generate_edges(self, size):
        for i in range(size):
            edge1 = []
            edge2 = []
            edge3 = []
            edge4 = []
            edge5 = []
            edge6 = []

            for j in range(size):
                edge1.append((i, j))
                edge2.append((j, i))

            for j in range(size - i):
                edge3.append((i + j, j))
                edge4.append((i + j, size - j - 1))

            for j in range(i + 1):
                edge5.append((i - j, j))
                edge6.append((i - j, size - j - 1))

            self.add_edge(edge1)
            self.add_edge(edge2)
            self.add_edge(edge3)
            self.add_edge(edge4)
            self.add_edge(edge5)
            self.add_edge(edge6)

    def count_points(self):
        points = 0
        edges_left = []

        for edge in self.edges:
            edge_completed = True
            for space in edge:
                if space not in self.placed:
                    edge_completed = False
                    break

            if edge_completed:
                points += len(edge)
            else:
                edges_left.append(edge)

        self.edges = edges_left

        return points

    def place(self, space):
        self.available.remove(space)
        self.placed.append(space)

        return self.count_points()

    def is_finished(self):
        return len(self.available) == 0

    def clone(self):
        new_stratego = Stratego(self.size)
        new_stratego.placed = deepcopy(self.placed)
        new_stratego.edges = deepcopy(self.edges)
        new_stratego.available = deepcopy(self.available)

        return new_stratego
