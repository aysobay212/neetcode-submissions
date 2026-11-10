class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        starting_nums = []
        for num in nums:
            if num-1 not in nums:
                starting_nums.append(num)
        
        best_length = 0
        for s_num in starting_nums:
            current_length = 1
            # keep incrementing until we cannot
            while s_num+1 in nums:
                s_num += 1
                current_length += 1
            if current_length > best_length:
                best_length = current_length
        return best_length