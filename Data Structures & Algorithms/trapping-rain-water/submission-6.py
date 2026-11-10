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


        





























#         # first identify the candidate walls
#         candidate_walls = [] # we will store the indices

#         # find all candidate walls which we can use
#         # this checks the existence of a left wall
#         for i in range(0, len(height)-1):
#             if (height[i] > 0 and height[i] > height[i+1]):
#                 candidate_walls.append(i)

#         # check existence for a right wall
#         right_wall = None
#         for i in range(len(height) - 1, -1, -1):
#             if height[i-1] < height[i]:
#                 right_wall = i
#                 break
#         if right_wall is None:
#             return 0 # No solution exists
#         for wall in candidate_walls:
#             if wall > right_wall:
#                 candidate_walls.remove(wall)

#         # now that we have our candidate walls in which we are
#         # able to fill in water, lets fill in the water between all
#         # bounds
#         p1 = 0
#         p2 = 1
#         capacity = 0

#         # compare each two walls
#         for _ in range(0, len(candidate_walls)-1):
            
#             # adjacent case
#             if abs(candidate_walls[p1] - candidate_walls[p2]) == 1:
#                 water = abs(height[candidate_walls[p1]] - height[candidate_walls[p2]])
#                 #print(water, candidate_walls[p1], candidate_walls[p2])

#             # 1 seperate case
#             elif abs(candidate_walls[p1] - candidate_walls[p2]) == 2:
#                 water = min(height[candidate_walls[p1]], height[candidate_walls[p2]])
#                 #print(water, candidate_walls[p1], candidate_walls[p2])
            
#             # span case
#             else:
#                 water = 0
#                 border = height[candidate_walls[p2]]
#                 for col in range(candidate_walls[p1]+1, candidate_walls[p2]):
                    
#                     water += border - height[col]
#                     print(border - height[col], border, height[col])

            

#             capacity += water
#             p1 += 1
#             p2 += 1
#         print(f"CAPACITY: {capacity}")
#         return capacity

