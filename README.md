# PathPilot AI
**Adaptive Robot Navigation & Path Optimization using Q-Learning**

A grid-world reinforcement-learning project. A tabular Q-Learning agent learns to navigate around obstacles; Pygame visualizes the route, and a breadth-first search (BFS) baseline provides a shortest-path comparison for this unit-cost grid.

## Run on Windows
Open PowerShell or the VS Code terminal in this folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

You do not need to activate the environment, so PowerShell execution-policy restrictions should not block the run. Alternatively, double-click `run_pathpilot.bat`.

## Verify the core logic (optional)
After installing requirements, run:

```powershell
.\.venv\Scripts\python.exe check_project.py
```

This checks training and route generation without opening the Pygame window.

## Project structure
- `main.py` — connects training, route comparison, and the visual simulation
- `src/environment.py` — grid-world and rewards
- `src/q_learning.py` — tabular Q-Learning agent
- `src/pathfinding.py` — BFS shortest-path baseline
- `src/visualization.py` — Pygame interface
- `check_project.py` — core-logic verification

## Controls
- Close the window or press `Esc` to exit.
- Press `R` to replay the route.

## Legend
Blue = start; green = goal; dark grey = obstacles; light blue = displayed route; orange = robot.

## Notes
The success rate is from the displayed training run. This is a grid-world prototype, not a physical robot controller. Test additional maps and seeds before making broad performance claims. The baseline is BFS, which finds a shortest path in this four-direction, equal-cost grid.

## CV bullet (edit to match your verified results)
**PathPilot AI — Reinforcement Learning Navigation Simulator**: Built a grid-world robot navigation environment, trained a tabular Q-Learning agent to avoid obstacles, visualized learned routes in Pygame, and compared route length with a shortest-path baseline.
