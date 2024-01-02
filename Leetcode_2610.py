class Solution:
    def findMatrix(self, nums):
        num_count = {}
        for i in nums:
            if i in num_count:
                num_count[i] += 1
            else:
                num_count[i] = 1
        
        max_freq = num_count[max(num_count, key=num_count.get)]
        ans = [[] for i in range(max_freq)]

        for i in nums:
            while num_count[i] > 0:
                ans[num_count[i]-1].append(i)
                num_count[i] -= 1
                
        return ans
            

sol = Solution()

nums = [1,3,4,1,2,3,1]

print(sol.findMatrix(nums))