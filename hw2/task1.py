from typing import List
def find_max_profit(S: List[int]):
    n = len(S)
    
    if n < 2:
        # There is only one price or no price at all
        return 0, None, None
    
    # Divide
    mid = n // 2
    left_max_profit, left_buy_day, left_sell_day = find_max_profit(S[:mid])
    right_max_profit, right_buy_day, right_sell_day = find_max_profit(S[mid:])

    # Find the minimum and maximum price in the left half and right half
    left_min_price = min(S[:mid])
    right_max_price = max(S[mid:])

    # Combine
    # The maximum profit is the maximum of the left, right, or combined maximum profit
    max_profit = max(left_max_profit, right_max_profit, right_max_price - left_min_price)

    if max_profit == left_max_profit:
        # The maximum profit is in the left half
        return left_max_profit, left_buy_day, left_sell_day
    elif max_profit == right_max_profit:
        # The maximum profit is in the right half
        return right_max_profit, right_buy_day + mid, right_sell_day + mid
    else:
        # The maximum profit spans the two halves
        buy_day = S.index(left_min_price, 0, mid)
        sell_day = S.index(right_max_price, mid)
        return max_profit, buy_day, sell_day


def main():
    # Ask the user for the input array
    S = list(map(int, input("Enter the stock prices separated by spaces: ").split()))
    
    # Call the maxProfit function to find the best time to buy and sell
    max_profit, buy_day, sell_day = find_max_profit(S)
    
    # Print the result
    print(f"The best time to buy is day {buy_day+1} and the best time to sell is day {sell_day+1}.")
    print(f"The maximum profit is ${max_profit}.")

if __name__ == '__main__':
    main()
