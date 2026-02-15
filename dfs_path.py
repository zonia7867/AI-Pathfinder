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

class DFS:
    def __init__(self, grid):
        self.grid = grid
        self.explored = set()
        self.frontier = []  
        self.parent = {}
        self.steps = []
        self.path = []

    def search(self, start, goal):
        self.explored.clear()
        self.frontier.clear()
        self.parent.clear()
        self.steps.clear()
        self.path.clear()

        if not self.grid.position_valid(*start) or not self.grid.position_valid(*goal):
            return None


        stack = [start]
        self.frontier.append(start)
        self.parent[start] = None

        while stack:
            curr = stack.pop()
            if curr in self.explored:
                if curr in self.frontier:
                    self.frontier.remove(curr)
                continue
            self.steps.append({
                'explored': self.explored.copy(),
                'frontier': self.frontier.copy(),
                'current': curr
            })

            if curr == goal:
                self.path = self.reconstruct_path(goal)
                return self.path

            self.explored.add(curr)
            if curr in self.frontier:
                self.frontier.remove(curr)
            neighbors = self.grid.get_neighbors(*curr)
            for neighbor in reversed(neighbors):
                if neighbor not in self.explored and neighbor not in self.frontier:
                    stack.append(neighbor)
                    self.frontier.append(neighbor)
                    if neighbor not in self.parent:
                        self.parent[neighbor] = curr

        return None 

    def reconstruct_path(self, goal):
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = self.parent.get(current)
        path.reverse()
        return path

    def get_steps(self):
        return self.steps

    def get_path(self):
        return self.path