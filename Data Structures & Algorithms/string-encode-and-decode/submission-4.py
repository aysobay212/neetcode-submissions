class Solution:

    def encode(self, strs: List[str]) -> str:
        all_strings = f"{len(strs)}#" # very first read is the number of strings
        for string in strs:
            encoded_string  = f"#{len(string)}#{string}"
            all_strings += encoded_string
        return all_strings


    def decode(self, s: str) -> List[str]:
        
        decoded_string = []

        # find how many strings there are to decode (avoids using a while loop)
        index_num_strs = s.find("#")
        length = s[0:index_num_strs]

        # update s without how many strings there are to decode
        s = s[len(length) + 1:]

        # decode `length` strings
        for _ in range(int(length)):

            # find length of the next string
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


