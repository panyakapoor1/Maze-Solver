import streamlit as st # type: ignore
import heapq

# Directions: Up, Down, Left, Right
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1

def reconstruct_path(came_from, end):
    path = []
    while end in came_from:
        path.append(end)
        end = came_from[end]
    return path[::-1]

def bfs(maze, start, end):
    queue = [start]
    visited = set()
    came_from = {}
    visited.add(start)
    while queue:
        current = queue.pop(0)
        if current == end:
            return reconstruct_path(came_from, end)
        for dx, dy in DIRS:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(maze, nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                came_from[(nx, ny)] = current
                queue.append((nx, ny))
    return None

def dfs(maze, start, end):
    stack = [start]
    visited = set()
    came_from = {}
    visited.add(start)
    while stack:
        current = stack.pop()
        if current == end:
            return reconstruct_path(came_from, end)
        for dx, dy in DIRS:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(maze, nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                came_from[(nx, ny)] = current
                stack.append((nx, ny))
    return None

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, end):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == end:
            return reconstruct_path(came_from, end)

        visited.add(current)

        for dx, dy in DIRS:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)
            if is_valid(maze, nx, ny) and neighbor not in visited:
                temp_g = g_score[current] + 1
                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g
                    f_score[neighbor] = temp_g + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None

# -------- STREAMLIT UI --------
st.set_page_config(layout="wide")
st.title("🧩 Maze Solver Visualizer")

rows = st.slider("Number of Rows", 5, 20, 10)
cols = st.slider("Number of Columns", 5, 20, 10)

if "maze" not in st.session_state or len(st.session_state.maze) != rows or len(st.session_state.maze[0]) != cols:
    st.session_state.maze = [[0 for _ in range(cols)] for _ in range(rows)]

start = st.selectbox("Start Cell", [(i, j) for i in range(rows) for j in range(cols)])
end = st.selectbox("End Cell", [(i, j) for i in range(rows) for j in range(cols)])
algo = st.selectbox("Choose Algorithm", ["BFS", "DFS", "A*"])

st.write("### Click cells below to toggle wall (⬛) or path (⬜)")

for i in range(rows):
    cols_list = st.columns(cols)
    for j in range(cols):
        cell = st.session_state.maze[i][j]
        cell_label = "⬛" if cell == 1 else "⬜"
        if (i, j) == start:
            cell_label = "🟩"
        elif (i, j) == end:
            cell_label = "🟥"

        if cols_list[j].button(cell_label, key=f"{i}_{j}"):
            if (i, j) != start and (i, j) != end:
                st.session_state.maze[i][j] = 0 if cell == 1 else 1
            st.rerun()

if st.button("🚀 Solve Maze"):
    with st.spinner("Solving..."):
        maze = st.session_state.maze
        if algo == "BFS":
            path = bfs(maze, start, end)
        elif algo == "DFS":
            path = dfs(maze, start, end)
        else:
            path = astar(maze, start, end)

        if path:
            st.success(f"✅ Path Found! Length: {len(path)}")
            for i in range(rows):
                cols_list = st.columns(cols)
                for j in range(cols):
                    cell = st.session_state.maze[i][j]
                    cell_label = "⬛" if cell == 1 else "⬜"
                    if (i, j) == start:
                        cell_label = "🟩"
                    elif (i, j) == end:
                        cell_label = "🟥"
                    elif (i, j) in path:
                        cell_label = "🟦"
                    cols_list[j].markdown(f"<div style='text-align: center; font-size:24px'>{cell_label}</div>", unsafe_allow_html=True)
        else:
            st.error("❌ No path found!")