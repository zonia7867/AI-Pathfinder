import heapq

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


class UCS:
    def __init__(self, grid):
        self.grid = grid
        self.explored = set()
        self.frontier = set()
        self.parent = {}
        self.cost = {}
        self.steps = []
        self.path = []

    def search(self, start, goal):
        self.explored.clear()
        self.frontier.clear()
        self.parent.clear()
        self.steps.clear()
        self.path.clear()
        self.cost.clear()

        if not self.grid.position_valid(*start) or not self.grid.position_valid(*goal):
            return None

        pq = []
        heapq.heappush(pq, (0, start))
        self.frontier.add(start)
        self.parent[start] = None
        self.cost[start] = 0

        while pq:
            curr_cost, current = heapq.heappop(pq)

            if current in self.explored:
                continue

            self.steps.append({
                'explored': self.explored.copy(),
                'frontier': self.frontier.copy(),
                'current': current
            })

            if current == goal:
                self.path = self.reconstruct_path(goal)
                return self.path

            self.explored.add(current)
            self.frontier.discard(current)

            for neighbor in self.grid.get_neighbors(*current):
                new_cost = curr_cost + 1
                if neighbor not in self.cost or new_cost < self.cost[neighbor]:
                    self.cost[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
                    self.frontier.add(neighbor)
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
