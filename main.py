from bfs_pathfinder import Grid, BFS
from visualizer import BFSVisualizer


def create_example_grid():
    width, height = 10, 10
    walls = set()
    for y in range(1, 7):
        walls.add((5, y))

    walls.add((3, 3))
    walls.add((3, 4))
    walls.add((7, 2))
    walls.add((7, 8))

    return Grid(width, height, walls)


def make_grid():
    width, height = 15, 15
    walls = set()

    for y in range(3, 12):
        walls.add((5, y))
    
    for x in range(7, 13):
        walls.add((x, 8))
    
    for y in range(3, 8):
        walls.add((10, y))
    

    walls.add((3, 5))
    walls.add((3, 6))
    walls.add((12, 3))
    walls.add((12, 4))

    return Grid(width, height, walls)



def print_menu():
    print("----- CHOOSE A SEARCH ALGORITHM -----")
    print("[1] Breadth-First Search (BFS)")
    print("[2] Depth-First Search (DFS)")
    print("[3] Uniform Cost Search (UCS)")
    print("[4] Depth-Limited Search (DLS)")
    print("[5] Iterative Deepening Search (IDS)")
    print("[6] Bidirectional Search (BDS)")


def main():
    print_menu()
    choice = input("\n Enter your choice: ").strip()

    if choice == "1":
        grid = make_grid()
        start = (1, 1)
        goal = (13, 13)
        visualizer = BFSVisualizer(grid, cell_size=40, step_delay=100)
        visualizer.visualize(start, goal)
    elif choice == "2":
        grid = make_grid()
        start = (1, 1)
        goal = (13, 13)
    elif choice == "3":
        grid = make_grid()
        start = (1, 1)
        goal = (13, 13)
    elif choice == "4":
        grid = make_grid()
        start = (1, 1)
        goal = (13, 13)
    elif choice == "5":
        grid = make_grid()
        start = (1, 1)
        goal = (13, 13)
    elif choice == "6":
        grid = make_grid()
        start = (1, 1)
        goal = (13, 13)
    else:
        print("Invalid choice. Select a valid option.")
        return
    

if __name__ == "__main__":
    main()