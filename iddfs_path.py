from dls_path import DLS

class IDDFS:
    def __init__(self, grid, max_depth=20):
        self.grid = grid
        self.max_depth = max_depth
        self.explored = set()
        self.steps = []
        self.path = []

    def search(self, start, goal):
        self.steps.clear()
        self.path.clear()

        for depth in range(self.max_depth):
            dls = DLS(self.grid, limit=depth)
            result = dls.search(start, goal)

            self.steps.extend(dls.get_steps())

            if result:
                self.path = result
                self.explored = dls.explored
                return result

        return None

    def get_steps(self):
        return self.steps

    def get_path(self):
        return self.path
