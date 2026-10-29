class RobotEnvironment:
    """Small grid-world environment for robot navigation."""
    def __init__(self, rows=5, cols=5):
        self.rows, self.cols = rows, cols
        self.start, self.goal = (0, 0), (4, 4)
        self.obstacles = {(1, 1), (1, 2), (2, 2), (3, 2)}
        self.robot_position = self.start
        self.actions = {"up": (-1, 0), "down": (1, 0),
                        "left": (0, -1), "right": (0, 1)}

    def reset(self):
        self.robot_position = self.start
        return self.robot_position

    def step(self, action):
        if action not in self.actions:
            raise ValueError(f"Invalid action: {action}")
        r, c = self.robot_position
        dr, dc = self.actions[action]
        nxt = (r + dr, c + dc)
        if not (0 <= nxt[0] < self.rows and 0 <= nxt[1] < self.cols):
            return self.robot_position, -5, False
        if nxt in self.obstacles:
            return self.robot_position, -5, False
        self.robot_position = nxt
        if nxt == self.goal:
            return nxt, 10, True
        return nxt, -1, False
