class Solution:
    def maxProfit(self, prices) -> int:

        profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
                #print('Day', i, 'Buying for', prices[i])
                #print('Day', i+1, 'Selling for', prices[i + 1])
                #print('Day', i+1, 'Profit from', prices[i + 1] - prices[i])
                
        return profit


ans = Solution()
prices = [7,1,5,3,6,4]

#print(prices)
print('Full profit', ans.maxProfit(prices))

    