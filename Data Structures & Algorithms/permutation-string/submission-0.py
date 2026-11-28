class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s1 is the permutation (target)
        s2 is where we loop over
        we know that the window must be a fixed size
        """
        if len(s2) < len(s1):
            return False

        master = {}
        for char in s1:
            if char in master.keys():
                master[char] += 1
            else:
                master[char] = 1

        p1 = 0
        p2 = len(s1)

        candidate = {}
        for char in s2[p1:p2]:
            if char in candidate.keys():
                candidate[char] += 1
            else:
                candidate[char] = 1

        while p2 <= len(s2):
            if master == candidate:
                return True
            
            # remove left character
            if candidate[s2[p1]] == 1:
                candidate.pop(s2[p1])
            else:
                candidate[s2[p1]] -= 1
            p1 += 1
            # add next character
            if p2 < len(s2):
                if s2[p2] in candidate:
                    candidate[s2[p2]] += 1
                else:
                    candidate[s2[p2]] = 1
            p2 += 1


        return False

        
        

        