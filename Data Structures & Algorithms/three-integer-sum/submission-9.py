class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # this solution is valid but it is not very efficient...
        
        nums.sort()
        
        sols = []
        for i in range(0, len(nums), 1):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val == 0:
                    found = [nums[i], nums[l], nums[r]]
                    if found not in sols:
                        sols.append(found)
                    
                    # there could be more than one solution so we can't `break`
                    l += 1
                    r -= 1

                    # avoid the duplicate solutions however
                    


                elif val < 0:
                    l += 1
                else: 
                    r -= 1
        return sols
                            

        