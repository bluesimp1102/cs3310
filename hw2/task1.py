def maxProfit(S):
    n = len(S)
    if n < 2:
        return 0, None, None
    
    left = 0
    right = n - 1
    mid = (left + right) // 2

    # Divide
    left_max_profit, left_start, left_end = maxProfit(S[:mid + 1])
    right_max_profit, right_start, right_end = maxProfit(S[mid + 1:])

    # Conquer
    # Max profit in left half, right half, or spanning both halves
    max_profit = max(left_max_profit, right_max_profit, S[right] - S[left])

    if max_profit == left_max_profit:
        return left_max_profit, left_start, left_end
    elif max_profit == right_max_profit:
        return right_max_profit, right_start + mid + 1, right_end + mid + 1
    else:
        return max_profit, left, right

def main():
    # Ask the user for the input array
    S = list(map(int, input("Enter the stock prices separated by spaces: ").split()))
    
    # Call the maxProfit function to find the best time to buy and sell
    max_profit, buy_day, sell_day = maxProfit(S)
    
    # Print the result
    print(f"The best time to buy is day {buy_day+1} and the best time to sell is day {sell_day+1}.")
    print(f"The maximum profit is ${max_profit}.")

if __name__ == '__main__':
    main()