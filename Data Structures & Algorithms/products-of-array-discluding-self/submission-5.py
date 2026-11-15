class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [0]
        suffix_prod = []

        product1 = 1
        product2 = 1
        pointer = len(nums) - 1

        # compute prefix_prod and suffix_prod
        for i in range(0, len(nums)-1, 1):
            product1 *= nums[i]
            product2 *= nums[pointer]

            prefix_prod.append(product1)
            suffix_prod.append(product2)
            pointer -= 1

        # reverse the list
        suffix_prod = suffix_prod[::-1]
        suffix_prod.append(0)

        # calculate resulting array        
        resulting_array = []
        for k in range(0, len(prefix_prod), 1):
            resulting_array.append(prefix_prod[k]*suffix_prod[k])
        resulting_array[0] = suffix_prod[0]
        resulting_array[-1] = prefix_prod[-1]
        return resulting_array
