class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        p1 = 0
        p2 = len(heights) - 1

        while p1 < p2:
            # formula to calculate water
            # given p2 > p1
            capacity = min(heights[p1], heights[p2]) * (p2 - p1)
            print(capacity, p1, p2)
            if capacity > best:
                best = capacity
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        
        return best
   