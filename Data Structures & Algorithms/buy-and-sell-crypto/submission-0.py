class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        best = 0
        smallest = prices[0]
        largest = prices[0]

        for i in range(0, len(prices) - 1, 1):
            smallest = min(prices[:i+1]) 
            largest = max(prices[i:])
            best = max(best, largest - smallest)
        
        return best
        