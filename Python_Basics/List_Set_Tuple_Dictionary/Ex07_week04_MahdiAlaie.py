matrix = [ [0, 0, 5],
           [0, 2, 0],
           [4, 0, 0]]
ShortMatrix={

}

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] > 0:

            ShortMatrix[(i, j)] = matrix[i][j]

print(ShortMatrix)