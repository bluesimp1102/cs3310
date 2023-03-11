def findTurningPoint(arr, left, right):
    # base case: when the subarray contains only one element
    if left == right:
        return arr[left], left
    
    # find the middle index
    mid = (left + right) // 2
    
    # if the middle element is greater than its neighboring elements
    # then it is the turning point
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid], mid
    
    # if the middle element is greater than its left neighbor
    # then the turning point must be in the right half of the array
    if arr[mid] > arr[mid-1]:
        return findTurningPoint(arr, mid+1, right)
    
    # otherwise, the turning point must be in the left half of the array
    else:
        return findTurningPoint(arr, left, mid-1)
    
def main():
    # read in a list of integers from the user
    arr = list(map(int, input("Enter a list of integers: ").split()))
    
    # find the turning point and its index in the list
    turning_val, turning_point = findTurningPoint(arr, 0, len(arr)-1)
    
    # print the turning point and its index
    print(f"The integer {turning_val} is the turning point and its index is {turning_point} (starting from zero).")

if __name__ == '__main__':
    main()

'''
The best case complexity is O(1) when the turning point is the middle element of the array. 
The worst case complexity is O(logn) when the array is perfectly balanced, i.e., the turning point is exactly in the middle of the array. 
The average complexity is also O(logn).
'''
