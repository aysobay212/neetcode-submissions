class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for string in strs:
            alphabet_array = [0]*26
            for c in string:
                alphabet_array[ord(c)-97] += 1
            
            tupled =tuple(alphabet_array)
            if tupled in hashmap.keys():
                hashmap[tupled].append(string)
            else:
                hashmap[tupled] = [string] 
            
        return [thing for thing in hashmap.values()]
        