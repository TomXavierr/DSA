"""Number of Laser Beams in a Bank"""

class Solution:
    def numberOfBeams(self, bank) :
        beams, temp = 0, 0
        for i in bank:
            n = i.count('1')
            if n == 0:
                continue
            beams += temp * n
            temp = n
        return beams

sol = Solution()

bank = ["011001","000000","010100","001000"]


print(sol.numberOfBeams(bank))