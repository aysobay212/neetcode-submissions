class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # treat temperatures as a stack

        if len(temperatures) == 1:
            return [0]
        
        stack = [0]
        resulting_array = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                resulting_array[idx] = i - idx

            stack.append(i)
        return resulting_array
        # keep decreasing add to stack?
        # if increased, pop until you can't?