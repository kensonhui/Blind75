class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        change = [-1 for i in range(0, amount + 1)]
        for i in range(0, len(coins)):
            if coins[i] <= amount:
                change[coins[i]] = 1
        for i in range(1, len(change)):
            if change[i] == 1:
                continue
            minchange = i + 1
            for j in range(0, len(coins)):
                if i - coins[j] >= 1 and change[i - coins[j]] != -1:
                    minchange = min(minchange, change[i - coins[j]] + 1)
            if minchange == i + 1:
                change[i] = -1
            else:
                change[i] = minchange
        return change[amount]
