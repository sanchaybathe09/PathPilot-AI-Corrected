import numpy as np


class QLearningAgent:
    """Tabular Q-Learning agent."""
    ACTION_NAMES = ["up", "down", "left", "right"]

    def __init__(self, rows, cols, learning_rate=0.1, discount_factor=0.95, seed=42):
        self.rows, self.cols = rows, cols
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.num_actions = len(self.ACTION_NAMES)
        self.q_table = np.zeros((rows, cols, self.num_actions), dtype=float)
        self.rng = np.random.default_rng(seed)

    def update(self, state, action, reward, next_state, done):
        r, c = state
        nr, nc = next_state
        current = self.q_table[r, c, action]
        future = 0.0 if done else float(np.max(self.q_table[nr, nc]))
        target = reward + self.discount_factor * future
        self.q_table[r, c, action] = current + self.learning_rate * (target - current)

    def choose_action(self, state, epsilon=0.1):
        r, c = state
        if self.rng.random() < epsilon:
            return int(self.rng.integers(self.num_actions))
        values = self.q_table[r, c]
        best = np.flatnonzero(values == values.max())
        return int(self.rng.choice(best))

    def train(self, environment, episodes=2500, max_steps=100):
        history, successes = [], 0
        for episode in range(episodes):
            state = environment.reset()
            total = 0
            epsilon = max(0.03, 1.0 - episode / (episodes * 0.85))
            for _ in range(max_steps):
                action = self.choose_action(state, epsilon)
                nxt, reward, done = environment.step(self.ACTION_NAMES[action])
                self.update(state, action, reward, nxt, done)
                state = nxt
                total += reward
                if done:
                    successes += 1
                    break
            history.append(total)
        return history, successes

    def find_route(self, environment, max_steps=50):
        state = environment.reset()
        route, visited = [state], {state}
        for _ in range(max_steps):
            r, c = state
            order = list(np.argsort(self.q_table[r, c])[::-1])
            moved = False
            for action in order:
                environment.robot_position = state
                nxt, reward, done = environment.step(self.ACTION_NAMES[int(action)])
                if nxt != state and nxt not in visited:
                    state = nxt
                    route.append(state)
                    visited.add(state)
                    moved = True
                    if done:
                        return route
                    break
            if not moved:
                break
        return route
