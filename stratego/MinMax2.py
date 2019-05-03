import time

from stratego import Stratego


class MinMax2:
    def __init__(self, max_time):
        self.max_time = max_time

    def evaluate_space(self, state: Stratego, p_space):
        points = 0

        for edge in state.available_edges:
            if state.positions[p_space] in state.edges[edge]:
                parts_placed = []

                for space in state.edges[edge]:
                    if state.positions.index(space) in state.placed:
                        parts_placed.append(space)

                edge_len = len(state.edges[edge])
                parts_placed_len = len(parts_placed)

                if parts_placed_len + 1 == edge_len:
                    points += edge_len
                elif edge_len - parts_placed_len == 2:
                    points -= edge_len

        return points

    def minimax(self, state, depth, maximizing, start_time):
        points = []
        added_depth = []
        leaf_states = []
        current_time = time.time()

        for space in state.available:
            stratego_clone = state.clone()
            points.append(self.evaluate_space(stratego_clone, space))
            stratego_clone.place(space)
            leaf_states.append(stratego_clone)
            added_depth.append(depth)

        if current_time - start_time < self.max_time:
            for i, space in enumerate(state.available):
                stratego_clone = leaf_states[i]
                if not stratego_clone.is_finished():
                    point_val = self.minimax(stratego_clone, depth + 1, not maximizing, start_time)
                    if point_val:
                        points[i] += point_val
                        added_depth[i] += depth + 1

        max_points = max(points)
        min_points = min(points)

        if maximizing:
            if depth == 0:
                max_indices = [index for index, value in enumerate(points) if value == max_points]
                min_depth = added_depth[max_indices[0]]
                chosen_index = max_indices[0]
                for i in max_indices:
                    if added_depth[i] < min_depth:
                        min_depth = added_depth[i]
                        chosen_index = i

                return state.available[max_indices[0]]
            return max_points
        else:
            return min_points

    def move(self, stratego):
        start_time = time.time_ns()
        space = self.minimax(stratego.clone(), 0, True, time.time())

        # for pre, fill, node in RenderTree(root):
        #     print("%s%s" % (pre, node.name))

        return stratego.place(space), space, time.time_ns() - start_time
