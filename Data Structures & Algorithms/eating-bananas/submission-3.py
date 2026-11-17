class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        # # fancy way to round up
        # hours_per_pile = h // len(piles) + (h % len(piles) > 0) 

        # # select the largest pile
        # largest_pile = max(piles)

        # max_bananas_per_hour = largest_pile // hours_per_pile + (largest_pile % hours_per_pile > 0)

        # # we have derived an upper bound, the question asks for a MINIMUM
        l = 1
        r = max(piles)

        while l <= r:
            m = l + (r-l)//2
            hours = sum(pile // m + (pile % m > 0) for pile in piles)
            if hours > h:
                l = m + 1
            else:
                r = m - 1

        return l
