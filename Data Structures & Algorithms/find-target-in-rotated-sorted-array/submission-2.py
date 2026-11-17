class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # same question as you just did, but now you have a target

        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]: # must be in the right half
                l = mid + 1
            else: # must be in the left half
                r = mid
        
        min_idx = l
        # we have found the minimum element which should be the start of the ascending sequence
        # now we run binary search on BOTH halves

        # BS on the right half
        l = min_idx
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        # BS on the left half
        l = 0
        r = min_idx
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
        