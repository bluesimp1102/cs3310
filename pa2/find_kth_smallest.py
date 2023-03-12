import random
from typing import List
def find_kth_smallest_1(k, S):
    n = len(S)
    if n == 1:
        return S[0]
    else:
        m = random.choice(S)
        S1 = [x for x in S if x < m]
        S2 = [x for x in S if x == m]
        S3 = [x for x in S if x > m]
        if len(S1) >= k:
            return find_kth_smallest_1(k, S1)
        elif len(S1) + len(S2) >= k:
            return m
        else:
            return find_kth_smallest_1(k - len(S1) - len(S2), S3)

def find_kth_smallest_2(k: int, S: List[int]):
    n = len(S)
    if n < 50:
        # sort the list and return the kth smallest element
        S.sort()
        return S[k-1]
    else:
        # divide S into 5-element sequences and sort them
        sublists = [sorted(S[i:i+5]) for i in range(0, n, 5)]
        # find the medians of the sublists
        medians = [sublist[2] for sublist in sublists if len(sublist) >= 3]
        # find the median of the medians
        m = find_kth_smallest_2(len(medians) // 2, medians)
        # partition S into S1, S2, and S3
        S1 = [x for x in S if x < m]
        S2 = [x for x in S if x == m]
        S3 = [x for x in S if x > m]
        # recursively call the algorithm on the appropriate partition
        if len(S1) >= k:
            return find_kth_smallest_2(k, S1)
        elif len(S1) + len(S2) >= k:
            return m
        else:
            return find_kth_smallest_2(k - len(S1) - len(S2), S3)      

'''
Algorithm #1 without using a temporary array for partitioning
'''
def find_kth_smallest_1_modified(k: int, S: List[int]):
    n = len(S)
    if n == 1:
        return S[0]
    else:
        pivot_index = random.randrange(n)
        pivot = S[pivot_index]
        i, j = 0, n - 1
        while i <= j:
            while S[i] < pivot:
                i += 1
            while S[j] > pivot:
                j -= 1
            if i <= j:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
        if k <= j + 1:
            return find_kth_smallest_1_modified(k, S[:j+1])
        elif k > i:
            return find_kth_smallest_1_modified(k - i, S[i:])
        else:
            return S[j+1]


'''
Algorithm #2 without using a temporary array for partitioning
'''
def find_kth_smallest_2_modified(k: int, S: List[int], left=0, right=None):
    # Set default value for right if not provided
    if right is None:
        right = len(S) - 1
    # Base case: less than 50 elements in the list
    if right - left < 50:
        # Sort the list and return the kth smallest element
        S[left:right+1] = sorted(S[left:right+1])
        return S[left+k-1]
    else:
        # Divide S into 5-element subsequences and sort them
        sublists = [sorted(S[i:i+5]) for i in range(left, right+1, 5)]

        # Find the medians of the sublists
        medians = [sublist[2] for sublist in sublists if len(sublist) >= 3]

        # Find the median of the medians
        m = find_kth_smallest_2_modified(len(medians) // 2, medians)

        # Partition S around the median value
        i = left
        j = right
        while True:
            while S[i] < m:
                i += 1
            while S[j] > m:
                j -= 1
            if i >= j:
                break
            S[i], S[j] = S[j], S[i]
            i += 1
            j -= 1

        # Recurse on the left partition if k is less than or equal to j
        if k <= j:
            return find_kth_smallest_2_modified(k, S, left, j)
        # Return the median value if k is between j and i
        elif k <= i:
            return m
        # Recurse on the right partition if k is greater than i
        else:
            return find_kth_smallest_2_modified(k, S, i, right)

def main():
    import time
    # generate a random set of integers
    MIN_SET_SIZE = 5
    MAX_SET_SIZE = 20
    S = [random.randint(0, 100) for _ in range(random.randint(MIN_SET_SIZE, MAX_SET_SIZE))]
    k = random.randint(1, (len(S))//2+1)
    print("Original set of integers:", S)  # print the original set
    # find the 5th smallest integer using the first algorithm
    start_time = time.time()
    result1 = find_kth_smallest_1(k, S.copy())
    stop_time = time.time()
    print(f"First algorithm:\nThe {k}th smallest integer is {result1} (CPU time: {stop_time-start_time:.6f}s)")
    # find the 5th smallest integer using the second algorithm
    start_time = time.time()
    result2 = find_kth_smallest_2(k, S.copy())
    stop_time = time.time()
    print(f"Second algorithm:\nThe {k}th smallest integer is {result2} (CPU time: {stop_time-start_time:.6f}s)")
    # find the 5th smallest integer using the first algorithm - modified (extra credit)
    start_time = time.time()
    result1 = find_kth_smallest_1_modified(k, S.copy())
    stop_time = time.time()
    print(f"First algorithm (modified):\nThe {k}th smallest integer is {result1} (CPU time: {stop_time-start_time:.6f}s)")
    # find the 5th smallest integer using the second algorithm - modified (extra credit)
    start_time = time.time()
    result2 = find_kth_smallest_2_modified(k, S.copy())
    stop_time = time.time()
    print(f"Second algorithm (modified):\nThe {k}th smallest integer is {result2} (CPU time: {stop_time-start_time:.6f}s)")

if __name__ == '__main__':
    main()