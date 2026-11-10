class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_arr = [1]

        prefix_products = 1
        for i in range(0, len(nums)-1):
            prefix_products *= nums[i]
            prefix_arr.append(prefix_products)
        
        suffix_arr = [1]

        suffix_products = 1
        for i in range(len(nums)-1, 0, -1):
            suffix_products *= nums[i]
            suffix_arr = [suffix_products] + suffix_arr
      
        resulting_array = []
        for i in range(0, len(nums)):
            resulting_array.append(prefix_arr[i] * suffix_arr[i])
        return resulting_array