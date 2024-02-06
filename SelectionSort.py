def selection_sort(list):
    for i in range(len(list)-1):
        min_index = i 
        for j in range(i+1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        if min_index != i:
            list[i], list[min_index] = list[min_index], list[i]

    return list


print(selection_sort([5,2,5,3,1,7,9,10,4,6]))
