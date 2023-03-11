from typing import List
def sum_target(A, v):
    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            if A[i] + A[j] == v:
                return True
    return False

def two_sum_divide_conquer(A:List[int], v):
    def two_sum_helper(left, right, v):
        if left >= right:
            return False
        mid = (left + right) // 2
        if two_sum_helper(left, mid, v) or two_sum_helper(mid+1, right, v):
            return True
        i, j = left, mid+1
        while i <= mid and j <= right:
            if A[i] + A[j] == v:
                return True
            elif A[i] + A[j] < v:
                i += 1
            else:
                j += 1
        return False
    
    return two_sum_helper(0, len(A)-1, v)

def two_sum_linear(A, v) -> bool:
    left, right = 0, len(A)-1
    while left < right:
        s = A[left] + A[right]
        if s == v:
            return True
        elif s < v:
            left += 1
        else:
            right -= 1
    return False


print(two_sum_divide_conquer([1, 2, 3], 5))

