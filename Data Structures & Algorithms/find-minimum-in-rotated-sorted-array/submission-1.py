class Solution:
    def findMin(self, nums: List[int]) -> int:

        # we want to find the start of the sorted sequence in the rotated sorted array
        # we can do this by binary searching satisfying arr[l] < arr[r]
        small = 1001
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]: # then the smallest number must be in the left half
                l = mid + 1
            else: # otherwise, the smallest number must be in the right half
                r = mid 
        return nums[l] 
        