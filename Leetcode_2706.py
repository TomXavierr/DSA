class Solution:
    def buyChoco(self, prices, money: int) -> int:
        sorted_prices = sorted(prices)
        total = sorted_prices[0] + sorted_prices[1]
        if total <= money:
            return money - total
        else:
            return money


sol = Solution()

print(sol.buyChoco([3,2,3], 3))