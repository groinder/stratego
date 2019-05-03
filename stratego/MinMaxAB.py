import time

from math import inf


class MinMaxAB:
    max_time = 2  # seconds

    def minimax(self, state, depth, maximizing, start_time, a, b):
        alfa = a
        beta = b
        points = []
        leaf_states = []
        current_time = time.time()

        for space in state.available:
            stratego_clone = state.clone()
            leaf_states.append(stratego_clone)
            point_val = stratego_clone.place(space)
            if maximizing:
                alfa = max(alfa, point_val)
                if alfa >= beta:
                    points.append(alfa)
                else:
                    points.append(point_val)
            else:
                beta = min(beta, point_val)
                if alfa >= beta:
                    points.append(beta)
                else:
                    points.append(point_val)

        for i, space in enumerate(state.available):
            stratego_clone = leaf_states[i]
            if not stratego_clone.is_finished() and current_time - start_time < self.max_time:
                point_val = self.minimax(stratego_clone, depth + 1, not maximizing, start_time, alfa, beta)
                points[i] += point_val
                if maximizing:
                    alfa = max(alfa, point_val)
                    if alfa >= beta:
                        points[i] += alfa
                    else:
                        points[i] += point_val
                else:
                    beta = min(beta, point_val)
                    if alfa >= beta:
                        points[i] += beta
                    else:
                        points[i] += point_val

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
