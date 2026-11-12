class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap.keys():
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        return_list = []
        for _ in range(0, k, 1):
            best_value, best_key = 0, nums[0]

            for key, value in hashmap.items():
                if value > best_value:
                    best_key = key
                    best_value = value
            return_list.append(best_key)
            hashmap.pop(best_key)
        
        return return_list
        