class Solution:
    def isPalindrome(self, s: str) -> bool:

        # ignore all non-alphanumeric characters, however this can be optimised

        # s = "".join(char.lower() for char in s if char.isalnum())
        # length = len(s)

        # for i in range(0, int(length/2), 1):
        #     if s[i] != s[-(i+1)]:
        #         return False
        
        # return True

        # 2 pointer structured appraoch
        length = len(s)

        l = 0
        r = length-1

        while l < r:
            while l< r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True




