class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        best = 0

        while l < r:
            found = min(heights[l], heights[r]) * (r-l)
            if found > best:
                best = found
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best 
        