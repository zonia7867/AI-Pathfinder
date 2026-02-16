from collections import deque

class Grid:
    def __init__(self, width, height, walls=None):
        self.width = width
        self.height = height
        self.walls = walls or set()

    def position_valid(self, x, y):
        return (0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.walls)

    def get_neighbors(self, x, y):
        neighbors = [
            (x, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
            (x, y + 1),
            (x - 1, y),
            (x - 1, y - 1),
        ]
        return [(nx, ny) for nx, ny in neighbors if self.position_valid(nx, ny)]


class BidirectionalSearch:
    def __init__(self, grid):
        self.grid = grid
        self.steps = []
        self.path = []
        self.explored = set()

    def search(self, start, goal):
        frontier_start = deque([start])
        frontier_goal = deque([goal])

        parent_start = {start: None}
        parent_goal = {goal: None}

        visited_start = {start}
        visited_goal = {goal}

        while frontier_start and frontier_goal:
            current_start = frontier_start.popleft()
            self.explored.add(current_start)

            if current_start in visited_goal:
                self.path = self.build_path(parent_start, parent_goal, current_start)
                return self.path

            for neighbor in self.grid.get_neighbors(*current_start):
                if neighbor not in visited_start:
                    visited_start.add(neighbor)
                    frontier_start.append(neighbor)
                    parent_start[neighbor] = current_start

            current_goal = frontier_goal.popleft()

            if current_goal in visited_start:
                self.path = self.build_path(parent_start, parent_goal, current_goal)
                return self.path

            for neighbor in self.grid.get_neighbors(*current_goal):
                if neighbor not in visited_goal:
                    visited_goal.add(neighbor)
                    frontier_goal.append(neighbor)
                    parent_goal[neighbor] = current_goal

        return None

    def build_path(self, parent_start, parent_goal, meeting):
        path = []

        node = meeting
        while node:
            path.append(node)
            node = parent_start[node]
        path.reverse()

        node = parent_goal[meeting]
        while node:
            path.append(node)
            node = parent_goal[node]

        return path

    def get_steps(self):
        return []

    def get_path(self):
        return self.path
