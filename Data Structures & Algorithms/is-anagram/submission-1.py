class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        construct a dictionary of s where keys are letters and values are frequency
        iterate over the characteres of t and subtract the frequency from the dictionary
        not an anagram if any value in the dictionary is non-zero
        """

        if len(s) != len(t):
            return False

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
