class Solution:

    def encode(self, strs: List[str]) -> str:
        all_strings = f"{len(strs)}#" # very first read is the number of strings
        for string in strs:
            encoded_string  = f"#{len(string)}#{string}"
            all_strings += encoded_string
        return all_strings


    def decode(self, s: str) -> List[str]:
        
        decoded_string = []

        index_num_strs = s.find("#")

        temp = s[0:index_num_strs]

        length = s[0:index_num_strs]
        num_of_strs = s[0]

        s = s[len(length) + 1:]
        print(temp)
        for _ in range(int(temp)):
            print(s)
            # find length of the next string
            #print(s)
            s = s[1:]
            index = s.find("#") 
            length = s[0:index]
            
            # update s to remove the length and separator
            s = s[len(length) + 1:]

            # obtain the next string 
            #print(s)
            next_string = s[0:int(length)]

            # update s
            s = s[int(length):]
            decoded_string.append(next_string)
        return decoded_string


