import pygame
from bfs_pathfinder import Grid, BFS


class PathVisualizer:
    COLORS = {
        'background': (220, 220, 220),
        'wall': (0, 0, 0),                
        'empty': (240, 240, 240),        
        'frontier': (255, 255, 0),        
        'explored': (173, 216, 230),     
        'path': (255, 165, 0),            
        'start': (0, 255, 0),             
        'goal': (255, 0, 0),              
        'current': (255, 215, 0),         
    }

    def __init__(self, grid, algo="BFS",cell_size=30, step_delay=50):
        pygame.init()

        self.grid = grid
        self.algo = algo
        self.cell_size = cell_size
        self.step_delay = step_delay
        self.width = grid.width * cell_size
        self.height = grid.height * cell_size
        self.info_height = 80

        self.screen = pygame.display.set_mode(
            (self.width, self.height + self.info_height)
        )
        pygame.display.set_caption(f"AI PATHFINDING VISUALIZER - {self.algo}")

        self.font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 20)

        self.pathfinder = None
        self.steps = []
        self.path = []
        self.start_pos = None
        self.goal_pos = None
        self.animation_step = 0

    def visualize(self, start, goal):
        self.start_pos = start
        self.goal_pos = goal
        self.pathfinder = BFS(self.grid)
        result = self.pathfinder.search(start, goal)

        self.steps = self.pathfinder.get_steps()
        self.path = self.pathfinder.get_path()

        self.print_search_results(result)

        clock = pygame.time.Clock()
        running = True
        animation_step = 0

        while running and animation_step < len(self.steps):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_state(animation_step)
            pygame.display.flip()
            clock.tick(1000 // self.step_delay)

            animation_step += 1


        if result:
            self.draw_final_state()
            pygame.display.flip()
            self.print_path_details()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(30)

        pygame.quit()


    def draw_state(self, step_index):
        self.screen.fill(self.COLORS['background'])

        step = self.steps[step_index] if step_index < len(self.steps) else {}
        explored = step.get('explored', set())
        frontier = step.get('frontier', set())
        current = step.get('current', None)

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                rect = pygame.Rect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )

                if (x, y) in self.grid.walls:
                    color = self.COLORS['wall']
                elif (x, y) == self.start_pos:
                    color = self.COLORS['start']
                elif (x, y) == self.goal_pos:
                    color = self.COLORS['goal']
                elif (x, y) == current:
                    color = self.COLORS['current']
                elif (x, y) in explored:
                    color = self.COLORS['explored']
                elif (x, y) in frontier:
                    color = self.COLORS['frontier']
                else:
                    color = self.COLORS['empty']

                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (150, 150, 150), rect, 1)  

        self.draw_info_panel(step_index, explored, frontier)

    def draw_final_state(self):
        self.screen.fill(self.COLORS['background'])
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                rect = pygame.Rect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )

                if (x, y) in self.grid.walls:
                    color = self.COLORS['wall']
                elif (x, y) == self.start_pos:
                    color = self.COLORS['start']
                elif (x, y) == self.goal_pos:
                    color = self.COLORS['goal']
                elif (x, y) in self.path:
                    color = self.COLORS['path']
                elif (x, y) in self.pathfinder.explored:
                    color = self.COLORS['explored']
                else:
                    color = self.COLORS['empty']

                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (150, 150, 150), rect, 1)

        self.draw_final_info_panel()

    def draw_info_panel(self, step_index, explored, frontier):
        info_rect = pygame.Rect(0, self.height, self.width, self.info_height)
        pygame.draw.rect(self.screen, (0,0,255), info_rect)
        pygame.draw.line(self.screen, (255, 255, 0), (0, self.height), (self.width, self.height), 3)

    
        title_text = self.title_font.render(f" {self.algo} Algorithm", True, (255, 255, 255))
        self.screen.blit(title_text, (10, self.height + 8))

        
        step_text = self.font.render(
            f"Step: {step_index + 1}/{len(self.steps)}",
            True, (255, 255, 255)
        )
        self.screen.blit(step_text, (10, self.height + 45))

        stats_text = self.small_font.render(
            f"Explored: {len(explored)} | Frontier: {len(frontier)}",
            True, (200, 200, 200)
        )
        self.screen.blit(stats_text, (10, self.height + 65))

    def draw_final_info_panel(self):
        info_rect = pygame.Rect(0, self.height, self.width, self.info_height)
        pygame.draw.rect(self.screen, (34, 139, 34), info_rect) 
        pygame.draw.line(self.screen, (255, 215, 0), (0, self.height), (self.width, self.height), 3)

        title_text = self.title_font.render("Path Found!", True, (255, 255, 255))
        self.screen.blit(title_text, (10, self.height + 8))

        path_length = len(self.path)
        stats1 = self.font.render(
            f"Path Length: {path_length} steps",
            True, (255, 255, 255)
        )
        self.screen.blit(stats1, (10, self.height + 45))

        stats2 = self.small_font.render(
            f"Total Explored: {len(self.pathfinder.explored)} nodes",
            True, (240, 240, 240)
        )
        self.screen.blit(stats2, (10, self.height + 65))

    def print_search_results(self, result):
        """Print search results"""
        print("\n SEARCH RESULTS:")
        print("─" * 70)
        if result:
            print("   Status         : PATH FOUND")
            print(f"   Path Length    : {len(self.path)} steps")
            print(f"   Nodes Explored : {len(self.pathfinder.explored)}")
            print(f"   Search Steps   : {len(self.steps)}")
        else:
            print("   Status         :  NO PATH FOUND")
            print(f"   Nodes Explored : {len(self.pathfinder.explored)}")
        print("─" * 70)

    def print_path_details(self):
        if self.path:
            print("\n  PATH DETAILS:")
            print("─" * 70)
            print("   Path Coordinates:")
            for i, pos in enumerate(self.path):
                if i % 5 == 0:
                    print(f"     ", end="")
                print(f"{pos}", end="  ")
                if (i + 1) % 5 == 0:
                    print()
            if len(self.path) % 5 != 0:
                print()
            print("─" * 70)

 