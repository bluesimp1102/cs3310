import random

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

def find_kth_smallest_2(k, S):
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
              
def main():
    import time
    # generate a random set of integers
    MIN_SET_SIZE = 5
    MAX_SET_SIZE = 20
    S = [random.randint(0, 100) for _ in range(random.randint(MIN_SET_SIZE, MAX_SET_SIZE))]
    k = random.randint(1, (len(S))//2+1)
    print(S)  # print the original set
    # find the 5th smallest integer using the first algorithm
    start_time = time.time()
    result1 = find_kth_smallest_1(k, S)
    stop_time = time.time()
    print(f"First algorithm:\nThe {k}th smallest integer is {result1} (CPU time: {stop_time-start_time:.6f}s)")

    # find the 5th smallest integer using the second algorithm
    start_time = time.time()
    result2 = find_kth_smallest_2(k, S)
    stop_time = time.time()
    print(f"Second algorithm:\nThe {k}th smallest integer is {result2} (CPU time: {stop_time-start_time:.6f}s)")

if __name__ == '__main__':
    main()