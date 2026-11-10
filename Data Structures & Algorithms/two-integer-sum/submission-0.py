class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                obtained_index = hashmap[difference]
                if obtained_index <= index:
                    return [obtained_index,index]
                else:
                    return [index,obtained_index]

            else:
                hashmap[num] = index
        return []