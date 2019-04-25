class Stratego:
    placed = []
    available = []
    edges = []

    def __init__(self, size):
        r = range(size)

        for i in r:
            for j in r:
                self.available.append((i, j))

        self.add_straight_edges(size)

        for i in range(len(self.available)):
            self.add_right_diagonal_edge(i, size)
            self.add_left_diagonal_edge(i, size)

            if len(self.edges) == size * 2 + ((size - 3) * 2):
                break

    def add_right_diagonal_edge(self, i, size):
        edge = []
        if i < size:
            for j in range(i, i + size * (size - i), size + 1):
                edge.append(self.available[j])
        elif i % size == 0:
            for j in range(i, i + size * (size - int(i / size)), size + 1):
                edge.append(self.available[j])

        if len(edge) > 1:
            self.edges.append(edge)

    def add_left_diagonal_edge(self, i, size):
        edge = []
        if i < size:
            for j in range(i, i * size + 1, size - 1):
                edge.append(self.available[j])
        elif i % size == size - 1:
            for j in range(i, i + (size - 1) * (size - int(i / size)), size - 1):
                edge.append(self.available[j])

        if len(edge) > 1:
            self.edges.append(edge)

    def add_straight_edges(self, size):
        for i in range(size):
            edge1 = []
            edge2 = []
            for j in range(size):
                edge1.append((i, j))
                edge2.append((j, i))

            self.edges.append(edge1)
            self.edges.append(edge2)

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
