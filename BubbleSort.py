def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            
    return list


print(bubble_sort([5,2,5,3,1,7,9,10,4,6]))