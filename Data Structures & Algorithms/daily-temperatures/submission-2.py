class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        
        if len(temperatures) == 1:
            return [0]

        results = [0 for _ in temperatures]
        stack_i = [0] # <- this is a monotonic stack (DECREASING)

        current_index = 1

        while current_index < len(temperatures): 
            current_temp = temperatures[current_index]
            stackk = [temperatures[i] for i in stack_i]
            print(f"cIndex: {temperatures[current_index]}, cTemp {current_temp}, stack: {stackk}, results: {results}")
            
            if len(stack_i) == 0:
                stack_temp = 101
            else:
                stack_temp = temperatures[stack_i[-1]]
            if stack_temp < current_temp:
                # keep popping from stack
                print(stack_i[-1], current_index)
                results[stack_i[-1]] = (current_index - stack_i[-1])
                stack_i.pop()
            else:
                # add to stack, increment
                stack_i.append(current_index)
                current_index += 1
        
        return results


            
