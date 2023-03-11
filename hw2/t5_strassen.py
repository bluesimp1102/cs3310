'''
This function implements Strassen's algorithm for matrix multiplication
'''
def strassenMatrixMultiply(a, b):
    n = len(a)
    # Base case: if the matrices are 1x1, simply return their product
    if n == 1:
        return [[a[0][0] * b[0][0]]]

    # Split the matrices into quadrants
    a11, a12, a21, a22 = split_matrix(a)
    b11, b12, b21, b22 = split_matrix(b)

    # Compute the seven matrix multiplications
    m1 = strassenMatrixMultiply(add_matrices(a11, a22), add_matrices(b11, b22))
    m2 = strassenMatrixMultiply(add_matrices(a21, a22), b11)
    m3 = strassenMatrixMultiply(a11, subtract_matrices(b12, b22))
    m4 = strassenMatrixMultiply(a22, subtract_matrices(b21, b11))
    m5 = strassenMatrixMultiply(add_matrices(a11, a12), b22)
    m6 = strassenMatrixMultiply(subtract_matrices(a21, a11), add_matrices(b11, b12))
    m7 = strassenMatrixMultiply(subtract_matrices(a12, a22), add_matrices(b21, b22))

    # Compute the four quadrants of the result matrix
    c1 = add_matrices(subtract_matrices(add_matrices(m1, m4), m5), m7)
    c2 = add_matrices(m3, m5)
    c3 = add_matrices(m2, m4)
    c4 = add_matrices(subtract_matrices(add_matrices(m1, m3), m2), m6)

    # Combine the quadrants into a single matrix and return
    return combine_matrices(c1, c2, c3, c4)

'''
This function splits a matrix into four quadrants
'''
def split_matrix(m):
    rows = len(m)
    cols = len(m[0])
    # Ensure the matrix is even-sized
    if rows % 2 != 0 or cols % 2 != 0:
        raise ValueError("Matrix size is not even")

    half_rows = rows // 2
    half_cols = cols // 2
    a = [[m[i][j] for j in range(half_cols)] for i in range(half_rows)]
    b = [[m[i][j] for j in range(half_cols, cols)] for i in range(half_rows)]
    c = [[m[i][j] for j in range(half_cols)] for i in range(half_rows, rows)]
    d = [[m[i][j] for j in range(half_cols, cols)] for i in range(half_rows, rows)]

    return a, b, c, d

'''
This function adds two matrices
'''
def add_matrices(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c

'''
This function subtracts two matrices
'''
def subtract_matrices(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]
    return c

'''
This function combines four matrices into a single matrix
'''
def combine_matrices(a11, a12, a21, a22):
    n = len(a11)
    m = [[0] * (n * 2) for _ in range(n * 2)]
    for i in range(n):
        for j in range(n):
            m[i][j] = a11[i][j]
            m[i][j + n] = a12[i][j]
            m[i + n][j] = a21[i][j]
            m[i + n][j + n] = a22[i][j]
    return m

def main():
    x = ([[2, 5, 7, 12], 
        [4, 1, 4, 2], 
        [5, 6, 3, 8],
        [1, 6, 7, 9]]
        )
    y = ([[1, 0, 2, 7], 
        [5, 9, 3, 4], 
        [6, 1, 2, 8],
        [1, 2, 8, 5]]
        )
    print(strassenMatrixMultiply(x, y))
    return
if __name__ == '__main__':
    main()