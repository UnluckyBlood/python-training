# Лучшее время для покупки и продажи акций
# Легко
# Темы
# Теги компании
# Подсказки
# Вам дан целочисленный массив prices, где prices[i] — цена NeetCoin в ith-й день.

# Вы можете выбрать один день, чтобы купить одну монету NeetCoin, и другой день в будущем, чтобы ее продать.

# Верните максимальную прибыль, которую вы можете получить. Вы можете не совершать никаких сделок, в этом случае прибыль составит 0.

# Пример 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Объяснение: купите prices[1] и продайте prices[4], profit = 7 - 1 = 6.

# Пример 2:

# Input: prices = [10,8,7,5,2]

# Output: 0
# Пояснение: прибыльных сделок совершить не удастся, поэтому максимальная прибыль равна 0.

# Ограничения:

# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100


def maxProfit(prices: List[int]) -> int:
    max_sell = 0
    min_prices = prices[0]
    for i in range(len(prices)):
        if min_prices > prices[i]:
            min_prices = prices[i]
        elif max_sell < (prices[i] - min_prices):
            max_sell = (prices[i] - min_prices)
    return max_sell
prices=[7,1,5,3,6,4]
print (maxProfit(prices))



# Быстрее на одну ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        maxp = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                prof = prices[r] - prices[l]
                maxp = max(maxp,prof)
            else:
                l = r
            r += 1
        return maxp
        