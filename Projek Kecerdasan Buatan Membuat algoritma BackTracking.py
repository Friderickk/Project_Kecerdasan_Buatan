def is_safe(maze, x, y, n, m, visited):
    if 0 <= x < n and 0 <= y < m and not visited[x][y] and maze[x][y] == 1:
        return True
    return False

def solve(maze, n, m, x, y, path, ans, visited):
    if x == n - 1 and y == m - 1:  # Reached the destination
        ans.append(path)
        return

    visited[x][y] = True  # Mark current cell as visited

    # Explore all four directions (down, up, left, right)
    for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
        if is_safe(maze, new_x, new_y, n, m, visited):
            path += 'D' if new_x == x + 1 else ('U' if new_x == x - 1 else ('L' if new_y == y - 1 else 'R'))
            solve(maze, n, m, new_x, new_y, path, ans, visited)
            path = path[:-1]  # Backtrack by removing the last direction

    visited[x][y] = False  # Mark current cell as unvisited (for other paths)

def possible_paths(maze):
    n = len(maze)
    m = len(maze[0])
    ans = []

    if maze[0][0] == 0 or maze[n - 1][m - 1] == 0:
        return ans

    visited = [[0] * m for _ in range(n)]  # Create a 2D list to store visited cells

    solve(maze, n, m, 0, 0, "", ans, visited)
    ans.sort()  # Sort the paths lexicographically

    return ans

# Example usage
maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
paths = possible_paths(maze)

for path in paths:
    print(path)