#32: matrix

matrix=[
	[1,3,5],
	[2,4,6],
]
print(matrix[0][2])
matrix[1][1]=10
print(matrix[1][1])

for row in matrix:
	for col in row:
		print(col)