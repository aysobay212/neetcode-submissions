class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        best = 0

        for i in range(0, len(prices) - 1, 1):
            smallest = min(prices[:i+1]) # find smallest up to the index
            largest = max(prices[i:]) # find the largest past the index
            best = max(best, largest - smallest)
        
        return best
        