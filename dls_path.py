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


class DLS:
    def __init__(self, grid, limit=10):
        self.grid = grid
        self.limit = limit
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

        stack = [(start, 0)]
        self.frontier.append(start)
        self.parent[start] = None

        while stack:
            current, depth = stack.pop()

            if current in self.explored:
                continue

            self.steps.append({
                'explored': self.explored.copy(),
                'frontier': set(self.frontier),
                'current': current
            })

            if current == goal:
                self.path = self.reconstruct_path(goal)
                return self.path

            self.explored.add(current)
            if current in self.frontier:
                self.frontier.remove(current)

            if depth < self.limit:
                neighbors = self.grid.get_neighbors(*current)
                for neighbor in reversed(neighbors):
                    if neighbor not in self.explored:
                        stack.append((neighbor, depth + 1))
                        self.frontier.append(neighbor)
                        self.parent[neighbor] = current

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
