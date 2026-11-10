class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i in range(0, len(nums), 1):
            differences[target - nums[i]] = i

        for i in range(0, len(nums), 1):
            if nums[i] in differences:
                j = differences[nums[i]]
                if i != j:
                    return [i, j]
        
 