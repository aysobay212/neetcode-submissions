class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums = sorted(nums) # sort the array, worst case O(n^2)

        for i in range(0, len(nums)):
            left = 0
            right = len(nums) - 1
            target = -nums[i]
            while left < right:
                print(left, right)
                if left == i:
                    left += 1
                elif right == i:
                    right -= 1
                else:
                    current_sum = nums[left] + nums[right] 
                    if current_sum > target:
                        right -= 1
                    elif current_sum == target:
                        triplet = sorted([nums[i], nums[left], nums[right]])
                        if triplet not in triplets:
                            triplets.append(triplet)
                        left += 1
                        right -= 1
                    else:
                        left += 1
                
        return triplets

            
        