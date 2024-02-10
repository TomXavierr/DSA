def twoSum(nums, target):
    # for i in range(len(list)):
    #     for j in range(i+1, len(list)):
    #         if list[i]+list[j] == target and i != j:
    #             return [i,j]


    prev_nums = {}
    for i,n in enumerate(nums):
        if target-n in prev_nums:
            return [i,prev_nums[target-n]]
        else:
            prev_nums[n] = i










print(twoSum([2,7,11,15],9))