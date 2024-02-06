class Solution:
    def buyChoco(self, prices, money: int) -> int:
        sorted_prices = sorted(prices)
        total = sorted_prices[0] + sorted_prices[1]
        if total <= money:
            return money - total
        else:
            return money

    def buyCandy(self, prices, money):
        lowest = min(prices)
        prices.remove(lowest)
        second_lowest = min(prices)

        balance = money - (lowest + second_lowest)

        return balance if balance >= 0 else money

    def buyChoco2(self, prices, money):
        lowest = second_lowest = float("inf")

        for price in prices:
            if price < lowest:
                lowest, second_lowest = price, lowest
            else:
                second_lowest = min(second_lowest, price)

        balance = money - (lowest + second_lowest)
        print("balance", balance)
        
        return balance if balance >= 0 else money



sol = Solution()

print(sol.buyChoco2([3,2,5], 10))