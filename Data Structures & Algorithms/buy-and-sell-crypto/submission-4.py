class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # original submission was O(n^2), we can try and beat this

        best = 0
        smallest = prices[0]

        for i in range(0, len(prices) - 1, 1):
            smallest = min(smallest, prices[i]) # find smallest up to the index
            largest = max(prices[i:]) # find the largest past the index
            best = max(best, largest - smallest)
        
        return best
        