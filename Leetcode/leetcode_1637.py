class Solution:
    def maxWidthOfVerticalArea(self, points) -> int:
        sorted_x = sorted([x for x, _ in points])

        max_width = 0

        for i in range(len(sorted_x)-1):
            if max_width < sorted_x[i+1] - sorted_x[i]:
                max_width = sorted_x[i+1] - sorted_x[i]

        return max_width


sol = Solution()

print(sol.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))