class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        has_count_one = any(value == 1 for value in count.values())
        if has_count_one:
            return -1

        for key, value in count.items():
            if value % 3 == 0:
                ops += value//3
            elif value % 3 == 1:
                ops += (value-4)//3 + 2
            else:
                ops += (value-2)//3 + 1 

        return ops

            

         

        
