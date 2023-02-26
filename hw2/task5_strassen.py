def strassen_matrix_multiply(a, b):
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]

    # Split the matrices into quadrants
    a11, a12, a21, a22 = split_matrix(a)
    b11, b12, b21, b22 = split_matrix(b)

    # Compute the seven matrix multiplications
    m1 = strassen_matrix_multiply(add_matrices(a11, a22), add_matrices(b11, b22))
    print("m1: ", m1)
    m2 = strassen_matrix_multiply(add_matrices(a21, a22), b11)
    print("m2: ", m2)
    m3 = strassen_matrix_multiply(a11, subtract_matrices(b12, b22))
    print("m3: ", m3)
    m4 = strassen_matrix_multiply(a22, subtract_matrices(b21, b11))
    print("m4: ", m4)
    m5 = strassen_matrix_multiply(add_matrices(a11, a12), b22)
    print("m5: ", m5)
    m6 = strassen_matrix_multiply(subtract_matrices(a21, a11), add_matrices(b11, b12))
    print("m6: ", m6)
    m7 = strassen_matrix_multiply(subtract_matrices(a12, a22), add_matrices(b21, b22))
    print("m7: ", m7)

    # Compute the four quadrants of the result matrix
    c1 = add_matrices(subtract_matrices(add_matrices(m1, m4), m5), m7)
    print("c1: ", c1)
    c2 = add_matrices(m3, m5)
    print("c2: ", c2)
    c3 = add_matrices(m2, m4)
    print("c3: ", c3)
    c4 = add_matrices(subtract_matrices(add_matrices(m1, m3), m2), m6)
    print("c4: ", c4)

    # Combine the quadrants into a single matrix and return
    return combine_matrices(c1, c2, c3, c4)


def split_matrix(m):
    rows = len(m)
    cols = len(m[0])
    if rows % 2 != 0 or cols % 2 != 0:
        raise ValueError("Matrix size is not even")
    half_rows = rows // 2
    half_cols = cols // 2
    a = [[m[i][j] for j in range(half_cols)] for i in range(half_rows)]
    b = [[m[i][j] for j in range(half_cols, cols)] for i in range(half_rows)]
    c = [[m[i][j] for j in range(half_cols)] for i in range(half_rows, rows)]
    d = [[m[i][j] for j in range(half_cols, cols)] for i in range(half_rows, rows)]
    # print(a, b, c, d)
    return a, b, c, d

def add_matrices(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c


def subtract_matrices(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]
    return c


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
    print(strassen_matrix_multiply(x, y))
    return
if __name__ == '__main__':
    main()