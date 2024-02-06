def merge(left_arr, right_arr):
    combined = []
    i = 0
    j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            combined.append(left_arr[i])
            i += 1
        else:
            combined.append(right_arr[j])
            j += 1
        
    while i < len(left_arr):
        combined.append(left_arr[i])
        i += 1
    while j < len(right_arr):
        combined.append(right_arr[j])
        j += 1

    return combined

def merge_sort(list):
    if len(list) == 1:
        return list
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return merge(merge_sort(left),merge_sort(right))


print(merge_sort([2,5,3,1,7,9,10,4,6]))