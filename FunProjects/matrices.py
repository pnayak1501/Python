
row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of columns: "))

matrix=[]
print("Enter the values in row: ")

# todo to put elements in a matrix
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrix.append(a)

# todo to print elements of a mtrix
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()
