def max_sum_partition(arr):
    if len(arr) == 1:
        return arr, []
    elif len(arr) == 2:
        return arr[:1], arr[1:]
    else:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        left1, right1 = max_sum_partition(left)
        left2, right2 = max_sum_partition(right)
        sum1, sum2 = sum(left1) + sum(right2), sum(left2) + sum(right1)
        return (left1 + right2, right1 + left2) if sum1 > sum2 else (left2 + right1, right2 + left1)
    
def main():
    arr = list(map(int, input("Enter a list of distinct positive integers: ").split()))
    sublist1, sublist2 = max_sum_partition(arr)
    print(f"Sublist 1: {sublist1}\nSublist 2: {sublist2}")

if __name__ == '__main__':
    main()