def findTurningPoint(arr, left, right):
    if left == right:
        return arr[left], left
    
    mid = (left + right) // 2
    
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid], mid
    
    if arr[mid] > arr[mid-1]:
        return findTurningPoint(arr, mid+1, right)
    else:
        return findTurningPoint(arr, left, mid-1)
    
def main():
    arr = list(map(int, input("Enter a list of integers: ").split()))
    turning_val, turning_point = findTurningPoint(arr, 0, len(arr)-1)
    print(f"The integer {turning_val} is the turning point and and its index = {turning_point} (starting from zero)")

if __name__ == '__main__':
    main()

'''
The best case complexity is O(1) when the turning point is the middle element of the array. The worst case complexity is O(logn) when the array is perfectly balanced, i.e., the turning point is exactly in the middle of the array. The average complexity is also O(logn).
'''