import time


class MinMax:
    max_depth = 2

    def minimax(self, state, depth, maximizing):
        points = []
        added_depth = []
        leaf_states = []

        for space in state.available:
            stratego_clone = state.clone()
            leaf_states.append(stratego_clone)
            point_val = stratego_clone.place(space)
            points.append(point_val)
            added_depth.append(depth)

        if depth < self.max_depth:
            for i, space in enumerate(state.available):
                stratego_clone = leaf_states[i]
                if not stratego_clone.is_finished():
                    point_val = self.minimax(stratego_clone, depth + 1, not maximizing)
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
        space = self.minimax(stratego.clone(), 0, True)

        # for pre, fill, node in RenderTree(root):
        #     print("%s%s" % (pre, node.name))

        return stratego.place(space), space, time.time_ns() - start_time
