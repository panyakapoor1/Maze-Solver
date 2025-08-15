# 🧩 Maze Solver Visualizer

A **Streamlit-based interactive maze solver** that allows you to design mazes and solve them using **BFS**, **DFS**, or **A\*** algorithms — with live visualization.

---

## 🚀 Features

- **Interactive Maze Creation**  
  - Click on cells to toggle between **wall** ⬛ and **path** ⬜.  
  - Choose **start** 🟩 and **end** 🟥 points.
- **Multiple Algorithms**  
  - **BFS** (Breadth-First Search) – shortest path in unweighted graphs.  
  - **DFS** (Depth-First Search) – explores paths deeply before backtracking.  
  - **A\*** Search – uses heuristics for efficient pathfinding.
- **Visual Path Display**  
  - Path cells are marked in **🟦** after solving.
- Adjustable **maze size** with sliders for rows and columns.

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/maze-solver.git
   cd maze-solver
   ```
2. Install dependencies:
```bash
pip install streamlit
```
## ▶️ Usage

Run the Streamlit app:
```bash
streamlit run app.py
```
- Adjust rows and columns using sliders.
- Select start and end cells from dropdown menus.
- Click on maze cells to create walls or paths.
- Choose the algorithm (BFS, DFS, or A*).
- Click 🚀 Solve Maze to visualize the solution.

## 📸 Example

**Maze before solving**<br>
⬜⬜⬜⬛⬜<br>
⬜🟩⬛⬛⬜<br>
⬜⬜⬜⬜🟥

**Maze after solving**<br>
⬜⬜⬜⬛⬜<br>
⬜🟩⬛⬛⬜<br>
⬜🟦🟦🟦🟥

## 🧠 Algorithms Overview

**1. BFS – Breadth-First Search**
- Explores equally in all directions.
- Guarantees the shortest path in unweighted graphs.

**2. DFS – Depth-First Search**
- Explores deeply before backtracking.
- May not find the shortest path, but useful for exploring.
  
***3. A* Search***
- Uses Manhattan distance as heuristic.
- Faster than BFS in most cases.

## 🛠 Tech Stack
- Python 3
- Streamlit – UI & visualization
- heapq – priority queue for A*

##💡 Future Improvements
- Add diagonal movement.
- Animate pathfinding step-by-step.
- Save/load maze configurations.

**Made with ❤️ using Python & Streamlit**
