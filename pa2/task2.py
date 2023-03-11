import random

def select_kth_smallest(k, S):
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
        m = select_kth_smallest(len(medians) // 2, medians)
        # partition S into S1, S2, and S3
        S1 = [x for x in S if x < m]
        S2 = [x for x in S if x == m]
        S3 = [x for x in S if x > m]
        # recursively call the algorithm on the appropriate partition
        if len(S1) >= k:
            return select_kth_smallest(k, S1)
        elif len(S1) + len(S2) >= k:
            return m
        else:
            return select_kth_smallest(k - len(S1) - len(S2), S3)

def main():
    import time

    # generate a random set of integers
    S = [random.randint(0, 100) for _ in range(100)]

    # find the 5th smallest integer using the first algorithm
    start_time = time.time()
    result1 = select_kth_smallest(5, S)
    print(f"First algorithm: {result1} (CPU time: {time.time()-start_time:.6f}s)")

    # find the 5th smallest integer using the second algorithm
    start_time = time.time()
    result2 = select_kth_smallest(5, S)
    print(f"Second algorithm: {result2} (CPU time: {time.time()-start_time:.6f}s)")

