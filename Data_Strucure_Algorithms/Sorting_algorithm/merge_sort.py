def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    #print(mid)
    left_half = arr[:mid]
    #print(left_half)
    right_half = arr[mid:]
    #print(left_half)

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

# Compare elements from the left and right halves and merge them
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            #print(merged)
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append the remaining elements, if any
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("given array:",arr)
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 34, 64, 90]

