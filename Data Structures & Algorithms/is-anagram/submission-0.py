class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_map = dict.fromkeys([c for c in s], 0)
        for c in s:
            s_map[c] += 1
        
        for c in t:
            if c in s_map:
                s_map[c] -= 1
            else:
                return False
        
        for value in s_map.values():
            if value != 0:
                return False
        
        return True
