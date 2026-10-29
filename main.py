import pygame
from src.environment import RobotEnvironment
from src.q_learning import QLearningAgent
from src.visualization import PathPilotVisualizer
from src.pathfinding import shortest_path


def main():
    env = RobotEnvironment()
    agent = QLearningAgent(env.rows, env.cols, seed=42)
    print("\n========== PATHPILOT AI ==========")
    print("Training Q-Learning agent...")
    rewards, successes = agent.train(env, episodes=2500, max_steps=100)
    success_rate = 100.0 * successes / len(rewards)
    route = agent.find_route(env, max_steps=50)
    baseline = shortest_path(env.rows, env.cols, env.start, env.goal, env.obstacles)
    route_ok = bool(route and route[-1] == env.goal)
    print("\n------------- RESULTS -------------")
    print(f"Training episodes:       {len(rewards)}")
    print(f"Successful episodes:     {successes}")
    print(f"Training success rate:   {success_rate:.1f}%")
    print(f"Q-Learning route found:  {'Yes' if route_ok else 'No'}")
    print(f"Q-Learning route steps:  {len(route)-1 if route_ok else 'N/A'}")
    print(f"Shortest-path baseline:  {len(baseline)-1 if baseline else 'N/A'} steps")
    print("Close the simulation window to exit; press R to replay.\n")

    shown_route = route if route_ok else baseline
    label = "Q-LEARNING" if route_ok else "SHORTEST-PATH FALLBACK"
    visual = PathPilotVisualizer(env.rows, env.cols, 100)
    visual.set_summary(success_rate, len(route)-1 if route_ok else None,
                       len(baseline)-1 if baseline else None, label)
    if not shown_route:
        shown_route = [env.start]

    running, index, frames = True, 0, 0
    reached = len(shown_route) <= 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    index, frames = 0, 0
                    reached = len(shown_route) <= 1
        if not reached and frames % 12 == 0:
            if index < len(shown_route)-1:
                index += 1
            reached = index >= len(shown_route)-1
        visual.draw_grid(env.start, env.goal, env.obstacles,
                         shown_route[:index+1], shown_route[index], reached)
        visual.clock.tick(30)
        frames += 1
    visual.close()


if __name__ == "__main__":
    main()
