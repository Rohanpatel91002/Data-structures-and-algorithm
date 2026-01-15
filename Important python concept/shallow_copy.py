grid = [[0] * 3] *3
grid[0][0] = 3

#print(id(grid[0]), id(grid[1]), id(grid[2]))

print(grid)

grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 3
print(grid)
