import sys

def flood_fill(grid, x, y, new_color):
    if grid[x][y] != 0:
        return
    stack = [(x, y)]
    rows, cols = len(grid), len(grid[0])
    while stack:
        cx, cy = stack.pop()
        if grid[cx][cy] == 0:
            grid[cx][cy] = new_color
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                    stack.append((nx, ny))

def find_next_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j
    return None

def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

def main():
    # Exemplo de entrada fixa
    grid = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0]
    ]
    print("Grid inicial:")
    print_grid(grid)

    color = 2
    while True:
        start = find_next_start(grid)
        if not start:
            break
        x, y = start
        flood_fill(grid, x, y, color)
        color += 1

    print("\nGrid preenchido:")
    print_grid(grid)