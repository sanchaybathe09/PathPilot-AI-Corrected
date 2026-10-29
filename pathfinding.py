from collections import deque


def shortest_path(rows, cols, start, goal, obstacles):
    """Shortest path for a four-direction unit-cost grid (BFS baseline)."""
    queue = deque([start])
    parents = {start: None}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for dr, dc in directions:
            nxt = (current[0] + dr, current[1] + dc)
            if not (0 <= nxt[0] < rows and 0 <= nxt[1] < cols):
                continue
            if nxt in obstacles or nxt in parents:
                continue
            parents[nxt] = current
            queue.append(nxt)
    if goal not in parents:
        return []
    path, node = [], goal
    while node is not None:
        path.append(node)
        node = parents[node]
    return list(reversed(path))
