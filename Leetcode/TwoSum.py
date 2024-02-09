def twoSum(list, target):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i]+list[j] == target and i != j:
                return [i,j]


print(twoSum([2,7,11,15],9))