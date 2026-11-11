class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for string in strs:
            alphabet_array = [0]*26
            for c in string:
                alphabet_array[ord(c)-97] += 1
            
            stringed =" ".join([str(x) for x in alphabet_array])
            if stringed in hashmap.keys():
                hashmap[stringed].append(string)
            else:
                hashmap[stringed] = [string] 
            
        return [thing for thing in hashmap.values()]
        