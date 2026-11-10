class Solution:
    def trap(self, height: List[int]) -> int:
        capacity = 0
        
        # find first wall to fill in from
        first_wall_index = None
        for i in range(0, len(height)):
            if height[i] > 0:
                first_wall_index = i
                break
        
        if first_wall_index is None: return capacity

        largest_wall_index = 0
        for i in range(0, len(height)):
            if height[i] > height[largest_wall_index]:
                largest_wall_index = i

        current_wall_index = first_wall_index
        temp_capacity = 0
        for i in range(first_wall_index+1, largest_wall_index+1):
            # the next wall is smaller
            if height[current_wall_index] > height[i]:
                temp_capacity += height[current_wall_index] - height[i]
            else:
                # then there is a pit we can fill
                capacity += temp_capacity
                temp_capacity = 0
                current_wall_index = i
        print(f"FC: {capacity, largest_wall_index}")
        # also try reverse if we don't catch everything on forward pass
        # find first wall to fill in from
        last_wall_index = None
        for i in range(len(height)-1, -1, -1):
            if height[i] > 0:
                last_wall_index = i
                break
        
        if last_wall_index is None: return capacity

        current_wall_index = last_wall_index
        temp_capacity = 0
        for j in range(last_wall_index-1, largest_wall_index -1, -1):
            # the previous wall is smaller
            if height[current_wall_index] > height[j]:
                print(height[current_wall_index], height[i], current_wall_index, height[current_wall_index] - height[j])
                temp_capacity += height[current_wall_index] - height[j]
            else:
                # then there is a pit we can fill
                capacity += temp_capacity
                temp_capacity = 0
                current_wall_index = j



        return capacity
