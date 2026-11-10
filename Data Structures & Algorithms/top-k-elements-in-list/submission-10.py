class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        
        # use hashmap to count the frequencies:
        hashmap = {}
        
        for num in nums: # initialise empty
            hashmap[num] = 0
        
        for num in nums:
            hashmap[num] += 1
        
        # use buckets to count 
        buckets = [[] for _ in range(0, len(nums)+1)]
        for key, value in hashmap.items():
            buckets[value].append(key)

        total_order = []
        for bucket_index in range(len(buckets)-1, -1, -1):
            if buckets[bucket_index] is not None:
                total_order += buckets[bucket_index]
        
        return total_order[0:k]
