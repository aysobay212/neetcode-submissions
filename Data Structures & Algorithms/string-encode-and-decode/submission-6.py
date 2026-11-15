class Solution:

    def encode(self, strs: List[str]) -> str:
        
        master_string = ""

        # encode length + string + terminal
        for s in strs:
            master_string += (f"{len(s)}#{s}")
        print(master_string)
        return master_string
            

    def decode(self, s: str) -> List[str]:
        
        output = []
        index = 0
        counter = 0

        # length#string format
        length = 0
        while index < len(s):
            
            counter = index 
            
            # final the terminal
            while s[counter] != "#":
             counter += 1

            length = int(s[index:counter]) # get length
            index = counter+1 # ignore the terminal

            # get string
            formed_string = s[index:index+length]
            output.append(formed_string)
            
            
            index += length # prepare for next string

        
        print(output)
        return output
        


        


