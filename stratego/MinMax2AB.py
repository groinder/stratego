import time

from math import inf

from stratego import Stratego


class MinMax2AB:
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

    def minimax(self, state, depth, maximizing, start_time, a, b):
        alpha = a
        beta = b
        if maximizing:
            points = [-inf for i in state.available]
        else:
            points = [inf for i in state.available]
        added_depth = []
        leaf_states = []
        current_time = time.time()

        for i, space in enumerate(state.available):
            stratego_clone = state.clone()
            point_val = self.evaluate_space(stratego_clone, space)
            stratego_clone.place(space)
            leaf_states.append(stratego_clone)
            added_depth.append(depth)
            if maximizing:
                if point_val > alpha:
                    alpha = point_val
                    points[i] = point_val
                if alpha >= beta:
                    points[i] = alpha
                    break
            else:
                if point_val < beta:
                    beta = point_val
                    points[i] = point_val
                if alpha >= beta:
                    points[i] = beta
                    break

        if current_time - start_time < self.max_time:
            for i, p in enumerate(points):
                stratego_clone = leaf_states[i]
                if not stratego_clone.is_finished():
                    point_val = self.minimax(stratego_clone, depth + 1, not maximizing, start_time, alpha, beta)
                    if maximizing:
                        if point_val > alpha:
                            alpha = point_val
                        if alpha >= beta:
                            points[i] += alpha
                            break
                    else:
                        if point_val < beta:
                            beta = point_val
                        if alpha >= beta:
                            points[i] += beta
                            break

        max_points = max(points)
        min_points = min(points)

        if maximizing:
            if depth == 0:
                return state.available[points.index(max_points)]
            return max_points
        else:
            return min_points

    def move(self, stratego):
        start_time = time.time_ns()
        space = self.minimax(stratego.clone(), 0, True, time.time(), -inf, inf)

        # for pre, fill, node in RenderTree(root):
        #     print("%s%s" % (pre, node.name))

        return stratego.place(space), space, time.time_ns() - start_time
