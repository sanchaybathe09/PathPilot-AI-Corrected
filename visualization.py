import pygame


class PathPilotVisualizer:
    """Pygame visualization for PathPilot AI."""
    def __init__(self, rows=5, cols=5, cell_size=100):
        pygame.init()
        self.rows, self.cols, self.cell_size = rows, cols, cell_size
        self.grid_height = rows * cell_size
        self.footer_height = 115
        self.width, self.height = cols * cell_size, self.grid_height + self.footer_height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("PathPilot AI | Adaptive Robot Navigation")
        self.clock = pygame.time.Clock()
        self.title_font = pygame.font.SysFont("Arial", 24, bold=True)
        self.body_font = pygame.font.SysFont("Arial", 17)
        self.small_font = pygame.font.SysFont("Arial", 14)
        self.grid_color = (200, 207, 218)
        self.obstacle_color = (57, 64, 77)
        self.start_color = (48, 112, 226)
        self.goal_color = (32, 165, 100)
        self.path_color = (178, 215, 255)
        self.robot_color = (244, 145, 35)
        self.text_color = (35, 43, 56)
        self.muted_color = (100, 110, 125)
        self.success_rate, self.q_steps, self.baseline_steps = 0.0, None, None
        self.route_label = "Q-LEARNING"

    def set_summary(self, success_rate, q_steps, baseline_steps, route_label):
        self.success_rate = success_rate
        self.q_steps = q_steps
        self.baseline_steps = baseline_steps
        self.route_label = route_label

    def draw_grid(self, start, goal, obstacles, route=None, robot_position=None, reached=False):
        self.screen.fill((245, 247, 250))
        route = route or []
        for r in range(self.rows):
            for c in range(self.cols):
                rect = pygame.Rect(c*self.cell_size, r*self.cell_size, self.cell_size, self.cell_size)
                pos = (r, c)
                color = self.start_color if pos == start else self.goal_color if pos == goal else self.obstacle_color if pos in obstacles else (255, 255, 255)
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, self.grid_color, rect, 2)
        if len(route) > 1:
            points = [(c*self.cell_size+self.cell_size//2, r*self.cell_size+self.cell_size//2) for r, c in route]
            pygame.draw.lines(self.screen, self.path_color, False, points, 8)
        if robot_position is not None:
            r, c = robot_position
            center = (c*self.cell_size+self.cell_size//2, r*self.cell_size+self.cell_size//2)
            pygame.draw.circle(self.screen, self.robot_color, center, self.cell_size//4)
            pygame.draw.circle(self.screen, (255, 255, 255), center, self.cell_size//4, 3)
        fy = self.grid_height
        pygame.draw.rect(self.screen, (239, 242, 247), pygame.Rect(0, fy, self.width, self.footer_height))
        self.screen.blit(self.title_font.render("PATHPILOT AI", True, self.text_color), (12, fy+7))
        status = "DESTINATION REACHED!" if reached else "ROBOT NAVIGATING..."
        color = self.goal_color if reached else (48, 100, 190)
        self.screen.blit(self.body_font.render(status, True, color), (12, fy+38))
        self.screen.blit(self.small_font.render(f"Training success rate: {self.success_rate:.1f}%", True, self.muted_color), (12, fy+64))
        qs = "N/A" if self.q_steps is None else str(self.q_steps)
        bs = "N/A" if self.baseline_steps is None else str(self.baseline_steps)
        line = f"Steps — Q-Learning: {qs} | Shortest-path baseline: {bs} | R: replay | Esc: quit"
        self.screen.blit(self.small_font.render(line, True, self.muted_color), (12, fy+86))
        pygame.display.flip()

    def close(self):
        pygame.quit()
