#generate list from 1 to 9
nums = []
for n in range(9):
    nums.append(n+1)

print(nums)

#now, generate 3x3 a grid

grid = []
for r in range(3):
    row = []
    for c in range(3):
        row.append(c)
    grid.append(row)

print(grid)

#good! now generate a 3 dimentional array 3x3x3

matrix = []
for z in range(3):
    z = []
    for y in range(3):
        y = []
        for x in range(3):
            y.append(x)
        z.append(y)
    matrix.append(z)

print(matrix) 

#now I understand how to generate multi-dimentional arrays using loops