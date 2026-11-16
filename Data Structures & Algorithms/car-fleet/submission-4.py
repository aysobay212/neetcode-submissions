class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        matched = []
        for i in range(0, len(position), 1):
            matched.append((position[i], speed[i]))
        matched = sorted(matched)
        # [furthest position from target, ..., closest position to target]
        
        # a stack, we simply check whether the top has a time <= the one before it
        times = []
        for car in matched:
            pos, speed = car
            time = (target - pos)/speed
            times.append(time)
        
        fleets = 1
        t1 = times.pop()
        while times:
            t2 = times.pop()
            if t2 > t1:
                fleets += 1
                t1 = t2
        return fleets
        
        # reading the solutions, an alternative approach is just to add items to the stack
        # IFF the time of the item you are adding on is > the top of the stack
        
        
        