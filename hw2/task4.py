def search_in_sorted_array(arr, target):
    m = len(arr)
    n = len(arr[0])
    i_start = 0
    i_end = m - 1
    j_start = 0
    j_end = n - 1
    
    # Search the middle row to find the row that the target is on
    i_mid = (i_start + i_end) // 2
    while i_start < i_end:
        if arr[i_mid][0] <= target <= arr[i_mid][-1]:
            break
        elif target < arr[i_mid][0]:
            i_end = i_mid - 1
        else:
            i_start = i_mid + 1
        i_mid = (i_start + i_end) // 2
    
    # If the target is not in the array, return (-1, -1) as "None"
    if not arr[i_mid][0] <= target <= arr[i_mid][-1]:
        return -1, -1
    
    # Search the row that the target is on using binary search
    j_mid = (j_start + j_end) // 2
    while j_start <= j_end:
        if arr[i_mid][j_mid] == target:
            return (i_mid, j_mid)
        elif arr[i_mid][j_mid] < target:
            j_start = j_mid + 1
        else:
            j_end = j_mid - 1
        j_mid = (j_start + j_end) // 2
    
    # If the target is not in the array, return (-1, -1) as "None"
    return -1, -1

import time
def main():
    arr = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [9, 10, 123]
    ]
    target=11
    start_time = time.time()
    i, j = search_in_sorted_array(arr, target)
    end_time = time.time()
    cpu_time = end_time - start_time
    if i == -1:
        print(f"Target {target} is not in the 2D array.\nCPU time = {cpu_time}")
    else:
        print(f"Target {target} is in the 2D array (i={i}, j={j})\nCPU time = {cpu_time}")

if __name__ == '__main__':
    main()