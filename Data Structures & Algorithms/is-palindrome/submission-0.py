class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1
        for _ in range(0, len(s)//2 + 1):
            print(s[a], s[b])
            if s[a].isalnum() and s[b].isalnum():
                if a < b:
                    if s[a].lower() != s[b].lower():
                        return False
                    a += 1
                    b -= 1
            else:

                if not s[a].isalnum():
                    a += 1
                if not s[b].isalnum():
                    b -= 1
        return True
            