class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        we can exploit the fact that the alphabet is of a fixed size
        keys in a dictionary are the frequency
        values are anagrams
        """

        hashmap = {}

        for string in strs:
            alphabet_array = [0]*26
            for c in string:
                alphabet_array[ord(c)-97] += 1 # ord('a') = 97
            
            tupled =tuple(alphabet_array) # convert to an immutable data structure that can be keyed
            if tupled in hashmap.keys():
                hashmap[tupled].append(string)
            else:
                hashmap[tupled] = [string] 
            
        return [thing for thing in hashmap.values()]
        