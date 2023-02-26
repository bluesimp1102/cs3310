import time

def maxSubSum1(a):
    max_sum = -float('inf')
    start_index, end_index = -1, -1
    for i in range(len(a)):
        for j in range(i, len(a)):
            this_sum = 0
            for k in range(i, j + 1):
                this_sum += a[k]
            if this_sum > max_sum:
                max_sum = this_sum
                start_index, end_index = i, j
    return max_sum, start_index, end_index

def maxSubSum2(a):
    max_sum = -float('inf')
    start_index, end_index = -1, -1
    for i in range(len(a)):
        this_sum = 0
        for j in range(i, len(a)):
            this_sum += a[j]
            if this_sum > max_sum:
                max_sum = this_sum
                start_index, end_index = i, j
    return max_sum, start_index, end_index

def maxSumRec(a, left, right):
    if left == right:
        # Base case
        return (a[left], left, right)

    center = (left + right) // 2
    maxLeftSum, maxLeftStart, maxLeftEnd = maxSumRec(a, left, center)
    maxRightSum, maxRightStart, maxRightEnd = maxSumRec(a, center + 1, right)
    maxLeftBorderSum = leftBorderSum = a[center]
    maxLeftBorderStart = center
    for i in range(center - 1, left - 1, -1):
        leftBorderSum += a[i]
        if leftBorderSum > maxLeftBorderSum:
            maxLeftBorderSum = leftBorderSum
            maxLeftBorderStart = i
    maxRightBorderSum = rightBorderSum = a[center + 1]
    maxRightBorderEnd = center + 1
    for i in range(center + 2, right + 1):
        rightBorderSum += a[i]
        if rightBorderSum > maxRightBorderSum:
            maxRightBorderSum = rightBorderSum
            maxRightBorderEnd = i
    maxBorderSum = maxLeftBorderSum + maxRightBorderSum
    if maxLeftSum >= maxRightSum and maxLeftSum >= maxBorderSum:
        return (maxLeftSum, maxLeftStart, maxLeftEnd)
    elif maxRightSum >= maxLeftSum and maxRightSum >= maxBorderSum:
        return (maxRightSum, maxRightStart, maxRightEnd)
    else:
        return (maxBorderSum, maxLeftBorderStart, maxRightBorderEnd)

def maxSubSumDP(a):
    n = len(a)
    max_sum = a[0]
    start_index = 0
    end_index = 0
    
    MS = [0] * n
    MS[0] = a[0]
    
    for i in range(1, n):
        if MS[i-1] > 0:
            MS[i] = MS[i-1] + a[i]
        else:
            MS[i] = a[i]
            start_index = i
        
        if MS[i] > max_sum:
            max_sum = MS[i]
            end_index = i
    
    return max_sum, start_index, end_index

import time

def main():
    a = list(map(int, input("Enter a list of integers: ").split()))

    # Algorithm 1
    start_time = time.time()
    max_sum_1, start_index, end_index = maxSubSum1(a)
    end_time = time.time()
    cpu_time_1 = end_time - start_time
    print(f"Algorithm 1: Max sum = {max_sum_1}, Start index = {start_index}, End index = {end_index}, CPU time = {cpu_time_1}")

    # Algorithm 2
    start_time = time.time()
    max_sum_2, start_index, end_index = maxSubSum2(a)
    end_time = time.time()
    cpu_time_2 = end_time - start_time
    print(f"Algorithm 2: Max sum = {max_sum_2}, Start index = {start_index}, End index = {end_index}, CPU time = {cpu_time_2}")

    # Algorithm 3
    start_time = time.time()
    max_sum_3, start_index, end_index = maxSumRec(a, 0, len(a)-1)
    end_time = time.time()
    cpu_time_3 = end_time - start_time
    print(f"Algorithm 3: Max sum = {max_sum_3}, Start index = {start_index}, End index = {end_index}, CPU time = {cpu_time_3}")

    # Algorithm 4
    start_time = time.time()
    max_sum_4, start_index, end_index = maxSubSumDP(a)
    end_time = time.time()
    cpu_time_4 = end_time - start_time
    print(f"Algorithm 4: Max sum = {max_sum_4}, Start index = {start_index}, End index = {end_index}, CPU time = {cpu_time_4}")

if __name__ == '__main__':
    main()