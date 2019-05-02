import time

from anytree import Node
from math import inf


class MinMax:
    max_time = 2  # seconds

    def minimax(self, node, maximizing, start_time):
        points = []
        current_time = time.time()

        for space in node.val.available:
            if current_time - start_time >= self.max_time:
                val = inf if maximizing else -inf
                points.append(val)
                continue

            stratego_clone = node.val.clone()
            point_val = stratego_clone.place(space)
            leaf = Node(space, parent=node, val=stratego_clone)
            if not stratego_clone.is_finished():
                point_val += self.minimax(leaf, not maximizing, start_time)

            points.append(point_val)

        max_points = max(points)
        min_points = min(points)

        if maximizing:
            if node.root == node:
                return node.val.available[points.index(max_points)]
            return max_points
        else:
            return min_points

    def generate_tree(self, node):
        # for pre, fill, node in RenderTree(node.root):
        #     print("%s%s" % (pre, node.name))

        for space in node.val.available:
            stratego_clone = node.val.clone()
            points = stratego_clone.place(space)
            leaf = Node(points, parent=node, val=stratego_clone)
            if not stratego_clone.is_finished():
                self.generate_tree(leaf)

            else:
                pass

    def move(self, stratego):
        root = Node("root", val=stratego.clone())
        start_time = time.time_ns()
        space = self.minimax(root, True, time.time())

        # for pre, fill, node in RenderTree(root):
        #     print("%s%s" % (pre, node.name))

        return stratego.place(space), space, time.time_ns() - start_time
