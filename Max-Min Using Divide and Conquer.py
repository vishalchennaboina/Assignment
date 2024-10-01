def find_max_min(arr, low, high):
    if low == high:  
        return arr[low], arr[low]
    
    if high == low + 1:  
        return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])
    
    mid = (low + high) // 2
    max1, min1 = find_max_min(arr, low, mid)
    max2, min2 = find_max_min(arr, mid + 1, high)
    
    return max(max1, max2), min(min1, min2)

#Example
arr = [12, 3, 5, 7, 19]
n = len(arr)
maximum, minimum = find_max_min(arr, 0, n - 1)
print("Maximum:", maximum)
print("Minimum:", minimum)