class Solution:
    def isPalindrome(self, s: str) -> bool:

        # ignore all non-alphanumeric characters, however this can be optimised
        
        s = "".join(char.lower() for char in s if char.isalnum())
        length = len(s)

        for i in range(0, int(length/2), 1):
            if s[i] != s[-(i+1)]:
                return False
        
        return True