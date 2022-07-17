class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        max_sale = 0
        max_price = 0
        for i in range(len(prices) - 1, -1, -1):
            max_sale = max(max_sale, max_price - prices[i])
            max_price = max(max_price, prices[i])
        return max_sale
            
