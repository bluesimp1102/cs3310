import random

def generate_board(n, m):
    # Generate a random n * m board with integer values between -10 and 10
    return [[random.randint(-10, 10) for _ in range(m)] for _ in range(n)]

def max_value_path(board):
    n, m = len(board), len(board[0])
    dp = [[0] * m for _ in range(n)]

    # Initialize the first cell
    dp[0][0] = board[0][0]

    # Initialize the first column
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + board[i][0]

    # Initialize the first row
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + board[0][j]

    # Fill in the remaining cells
    for i in range(1, n):
        for j in range(1, m):
            # Choose the maximum value from the cell to the left, the cell above, and the cell diagonally up and left
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + board[i][j]

    # Reconstruct the path
    path = []
    i, j = n - 1, m - 1

    # Backtrack from the bottom-right cell to the top-left cell
    while i > 0 or j > 0:
        path.append((i, j))
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            # Choose the direction with the maximum value
            max_prev = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            if max_prev == dp[i - 1][j]:
                i -= 1
            elif max_prev == dp[i][j - 1]:
                j -= 1
            else:
                i -= 1
                j -= 1

    path.append((0, 0))
    path.reverse()

    return dp[-1][-1], path

def main():
    n, m = 5, 5
    board = generate_board(n, m)
    print("Board:")
    for row in board:
        print(row)

    max_value, path = max_value_path(board)
    print("Max value:", max_value)
    print("Path:", path)

if __name__ == "__main__":
    main()


'''
This code generates a random n * m board with integer values between -10 and 10. 

It uses dynamic programming to find the maximum total values and the path that generates the maximum. 

The time complexity of this implementation is O(n*m), where n and m are the dimensions of the board.
'''