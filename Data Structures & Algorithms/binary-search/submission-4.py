class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lower = 0
        upper = len(nums) - 1

        if upper == lower:
            if nums[0] == target:
                return upper
            else:
                return -1
        

        while lower <= upper:
            chosen = ((lower + upper)//2)
            if nums[chosen] < target:
                lower = chosen + 1
            elif nums[chosen] > target:
                upper = chosen - 1
            else:
                return chosen
        return -1

        
        