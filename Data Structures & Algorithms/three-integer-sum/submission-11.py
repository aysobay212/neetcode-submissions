class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # this solution is valid but it is not very efficient...
        
        nums.sort()
        
        sols = []
        for i in range(0, len(nums), 1):

            # avoid duplicates first item 
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val == 0:
                    found = [nums[i], nums[l], nums[r]]
                    #if found not in sols: # avoid the duplicate solutions however this is not efficient
                    sols.append(found)
                    
                    # there could be more than one solution so we can't `break`
                    l += 1
                    r -= 1

                    # from the suggested solutions, we traverse L->R if we encounter a duplicate solution
                    while l < r and nums[l] == nums[l-1]:
                        l += 1


                elif val < 0:
                    l += 1
                else: 
                    r -= 1
        return sols
                            

        