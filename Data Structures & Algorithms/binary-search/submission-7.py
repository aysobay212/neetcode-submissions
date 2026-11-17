class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            idx = l + (r-l)//2  # the +l at the start counts for RELATIVE midpoint
            if target == nums[idx]:
                return idx
            elif nums[idx] < target:
                l = idx + 1
            else:  
                r = idx - 1
        return -1
        
        