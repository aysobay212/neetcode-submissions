class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        set_array = set(nums) # this also sorts ascendingly
        print(set_array)
    
        # we just simply check whether the previous guy exists
        best = 0
        current = 1
        for num in set_array:
            if num - 1 not in set_array:

                current = num
                count = 1

                while current + 1 in set_array:
                    current += 1
                    count += 1

                best = max(best, count)
        return best
    
       
       