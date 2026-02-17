from bfs_pathfinder import Grid, BFS
from dfs_path import DFS
from ucs_path import UCS
from dls_path import DLS
from iddfs_path import IDDFS
from bidirectional_path import BidirectionalSearch
from visualizer import PathVisualizer
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
    grid = make_grid()
    start = (1, 1)
    goal = (13, 13)

    if choice == "1":
        visualizer = PathVisualizer(grid, algo="BFS", cell_size=40, step_delay=100)
        visualizer.visualize(start, goal)
    elif choice == "2":
        visualizer = PathVisualizer(grid, algo="DFS", cell_size=40, step_delay=100)
        visualizer.visualize(start, goal)
    elif choice == "3":
        visualizer = PathVisualizer(grid, algo="UCS", cell_size=40, step_delay=100)
        visualizer.visualize(start, goal)
    elif choice == "4":
        visualizer = PathVisualizer(grid, algo="DLS", cell_size=40, step_delay=100)
        visualizer.visualize(start, goal)
    elif choice == "5":
        visualizer = PathVisualizer(grid, algo="IDS", cell_size=40, step_delay=100)
        visualizer.visualize(start, goal)
    elif choice == "6":
        visualizer = PathVisualizer(grid, algo="BDS", cell_size=40, step_delay=100)
        visualizer.visualize(start, goal)
    else:
        print("Invalid choice. Select a valid option.")
        return

if __name__ == "__main__":
    main()
