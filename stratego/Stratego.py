class Stratego:
    def __init__(self, size=4, placed=(), available=(), positions=None, edges=None, available_edges=()):
        self.size = size
        self.placed = placed
        self.available = available
        self.available_edges = available_edges

        if positions is None:
            self.positions = []
            r = range(size)

            idx = 0
            for i in r:
                for j in r:
                    new = (i, j)
                    if new not in self.positions:
                        self.positions.append(new)
                        self.available += (idx,)
                        idx += 1
        else:
            self.positions = positions

        if edges is None:
            self.edges = []
            self.generate_edges(size)

            self.available_edges = ()
            for i, edge in enumerate(self.edges):
                self.available_edges += (i,)
        else:
            self.edges = edges

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
        available_edges_left = []

        for edge in self.available_edges:
            edge_completed = True
            for space in self.edges[edge]:
                if self.positions.index(space) not in self.placed:
                    edge_completed = False
                    break

            if edge_completed:
                points += len(self.edges[edge])
            else:
                available_edges_left.append(edge)

        self.available_edges = tuple(available_edges_left)

        return points

    def place(self, space):
        self.available = tuple(x for x in self.available if x != space)
        self.placed += (space,)

        return self.count_points()

    def is_finished(self):
        return len(self.available) == 0

    def clone(self):
        return Stratego(self.size, self.placed, self.available, self.positions, self.edges, self.available_edges)
