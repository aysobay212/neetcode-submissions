class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        r = 0
        best = 0

        while r < len(s):
            # check if s[r] is in the hashset
            letter_to_add = s[r]
            if letter_to_add not in hashset:
                hashset.add(letter_to_add)
                r += 1
                best = max(best, r-l)
            else: # we did not add a new character
                hashset.remove(s[l])                
                l += 1

        return best