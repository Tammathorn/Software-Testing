def grid_challenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    for i in range(len(grid[0])):
        for j in range(1, len(grid)):
            if grid[j][i] < grid[j-1][i]:
                return "NO"
    return "YES"