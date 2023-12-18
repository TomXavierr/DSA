import sys

class Solution:
    def maxProductDifference(self, nums) -> int:
        min1 = min2 = sys.maxsize
        max1 = max2 = -sys.maxsize - 1

        for num in nums:
            if num <= min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
            if num >= max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num
        return max1*max2 - min1*min2


solution =  Solution()

print(solution.maxProductDifference([5,6,2,7,4]))