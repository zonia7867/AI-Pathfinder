# AI Pathfinder — Uninformed Search Visualization

> A real-time grid pathfinding visualizer built with Python and Pygame.
> Watch 6 classic search algorithms think, explore, and find their way.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.5-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)


<img width="612" height="707" alt="image" src="https://github.com/user-attachments/assets/11e333ed-6d51-4e22-a4c2-95c9e96ad59b" />

---

##  What Is This?

This project implements **six uninformed (blind) search algorithms** that navigate a 15×15 grid from a **Start node (S)** to a **Goal node (T)** while avoiding walls.

The key feature is the **step-by-step animation** — you can watch each algorithm explore the grid in real time, seeing exactly which nodes it checks, which it skips, and the final path it chooses.

---

##  Algorithms Implemented

| # | Algorithm | Strategy | Optimal? | Complete? |
|---|-----------|----------|----------|-----------|
| 1 | **BFS** | Breadth-First Search |  Yes |  Yes |
| 2 | **DFS** | Depth-First Search |  No |  No |
| 3 | **UCS** | Uniform-Cost Search |  Yes |  Yes |
| 4 | **DLS** | Depth-Limited Search |  No |  No |
| 5 | **IDDFS** | Iterative Deepening DFS |  Yes |  Yes |
| 6 | **Bidirectional** | Bidirectional BFS |  Yes |  Yes |

---

##  Visual Color Guide

| Color | Meaning |
|-------|---------|
|  Green | Start position |
|  Red | Goal position |
|  Yellow | Frontier — nodes waiting to be explored |
|  Light Blue | Explored — nodes already visited |
|  Orange | Final path from Start to Goal |
|  Gold | Currently processing node |
|  Black | Static wall (obstacle) |

---

##  Project Structure

```
AI-Pathfinder/
│
├── main.py                   # Entry point — menu to pick algorithm
├── visualizer.py             # Unified Pygame GUI for all algorithms
│
├── bfs_pathfinder.py         # Breadth-First Search
├── dfs_path.py               # Depth-First Search
├── ucs_path.py               # Uniform-Cost Search
├── dls_path.py               # Depth-Limited Search
├── iddfs_path.py             # Iterative Deepening DFS
├── bidirectional_path.py     # Bidirectional Search
│
├── requirements.txt          # Python dependencies
├── .gitignore                # Excludes __pycache__, .pyc files
└── README.md                 # This file
```

---

##  Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip

### Step 1 — Clone the repository
```bash
git clone https://github.com/zonia7867/AI-Pathfinder.git
cd AI-Pathfinder
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

Or install directly:
```bash
pip install pygame
```

### Step 3 — Run the program
```bash
python main.py
```

---

##  How to Use

1. Run `python main.py`
2. A menu appears in the terminal — choose an algorithm (1–6)
3. A Pygame window opens showing the 15×15 grid
4. Watch the algorithm explore step by step
5. Orange path appears when the goal is found
6. Close the window when done

```
<img width="944" height="373" alt="image" src="https://github.com/user-attachments/assets/fcbcd2f6-abc3-40d0-b685-261b83409297" />

```

---

##  Movement Order

All algorithms expand neighbors in this strict **clockwise order**:

```
↖ (6)  ↑ (1)   ✕
← (5)  [S]   → (2)
  ✕    ↓ (3)  ↘ (4)
```

| Step | Direction | Delta |
|------|-----------|-------|
| 1 | Up | (0, -1) |
| 2 | Right | (+1, 0) |
| 3 | Bottom | (0, +1) |
| 4 | Bottom-Right | (+1, +1) |
| 5 | Left | (-1, 0) |
| 6 | Top-Left | (-1, -1) |

> Top-Right and Bottom-Left diagonals are **not** used.

---

##  Algorithm Summary

### BFS — Breadth-First Search
Explores all nodes at the current depth before going deeper. Uses a **FIFO queue**. Guaranteed to find the shortest path in unweighted graphs.

### DFS — Depth-First Search
Plunges as deep as possible before backtracking. Uses a **LIFO stack**. Memory efficient but doesn't guarantee the shortest path.

### UCS — Uniform-Cost Search
Expands the node with the **lowest cumulative cost** first. Uses a **min-heap**. Straight moves cost `1.0`, diagonal moves cost `1.414` (√2). Optimal for weighted grids.

### DLS — Depth-Limited Search
DFS with a hard **depth cap** (default: 15). Prevents infinite loops but will fail if the goal is beyond the limit.

### IDDFS — Iterative Deepening DFS
Runs DLS repeatedly with increasing depth limits (0 → 1 → 2 → ...). Combines **BFS optimality** with **DFS memory efficiency**.

### Bidirectional Search
Runs two simultaneous BFS searches — one from Start, one from Goal — and stops when they meet. Explores roughly `O(b^(d/2))` nodes instead of `O(b^d)`.

---

##  Complexity Comparison

| Algorithm | Time | Space | 
|-----------|------|-------|
| BFS | O(b^d) | O(b^d) 
| DFS | O(b^m) | O(bm)
| UCS | O(b^d) | O(b^d) 
| DLS | O(b^l) | O(bl) 
| IDDFS | O(b^d) | O(bd) 
| Bidirectional | O(b^d/2) | O(b^d/2) 

`b` = branching factor · `d` = solution depth · `m` = max depth · `l` = depth limit

---

##  Tech Stack

- **Language:** Python 3.11
- **GUI:** Pygame 2.5
- **IDE:** VS Code
- **Version Control:** Git + GitHub

---

##  Read More

I wrote a detailed breakdown of this project on Medium:

 **https://medium.com/@f230801/teaching-an-ai-to-find-its-way-e36c4a05ede4**

Covers each algorithm's logic, visual patterns, and what I learned building this from scratch.

---

##  Notes

- `__pycache__` is excluded via `.gitignore` — do not commit it
- DLS may report "no path found" if depth limit is set too low — adjustable in `dls_path.py`
- Window stays open after search completes — close it manually

---



## 👤 Author

**Zonia Amer**
- GitHub: [@zonia7867](https://github.com/zonia7867)
**Maidah Nasir**
- GitHub: https://github.com/Maidah609 

---

> *"The only difference between these six algorithms is which node they pull out of the frontier next."*
