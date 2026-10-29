"""Quick check for PathPilot AI core logic (does not launch Pygame)."""
from src.environment import RobotEnvironment
from src.q_learning import QLearningAgent
from src.pathfinding import shortest_path


def main():
    env = RobotEnvironment()
    agent = QLearningAgent(env.rows, env.cols, seed=42)
    rewards, successes = agent.train(env, episodes=2500, max_steps=100)
    route = agent.find_route(env, max_steps=50)
    baseline = shortest_path(env.rows, env.cols, env.start, env.goal, env.obstacles)
    rate = 100 * successes / len(rewards)
    print(f"Training episodes: {len(rewards)}")
    print(f"Successful episodes: {successes}")
    print(f"Training success rate: {rate:.1f}%")
    print(f"Q-Learning route: {route}")
    print(f"BFS shortest route: {baseline}")
    assert route and route[0] == env.start and route[-1] == env.goal, "Q-Learning did not find a complete route"
    assert baseline and baseline[0] == env.start and baseline[-1] == env.goal, "BFS did not find a complete route"
    assert not any(cell in env.obstacles for cell in route), "Q-Learning route crosses an obstacle"
    print("CORE CHECK PASSED")


if __name__ == "__main__":
    main()
