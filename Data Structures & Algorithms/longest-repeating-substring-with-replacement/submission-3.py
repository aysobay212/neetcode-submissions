class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        i needed the solution video for this.
        p1 and p2 start at the first character and while window - most_freq <= k, move p2, otherwise move   
        p1
        """

        p1 = 0
        p2 = 0
        hash_table = {s[p2]:1} # freq
        best = k
        most_frequent = 1

        while p2 < len(s):
            
            # find the most frequent character in the hash table            
            for value in hash_table.values(): # O(26)
                most_frequent = max(most_frequent, value)

            window_length = p2 - p1 + 1 # +1 for 0-based indexing

            if window_length - most_frequent <= k:
                best = max(best, window_length)
                p2 += 1
                # update frequencies
                if p2 < len(s):
                    if s[p2] not in hash_table:
                        hash_table[s[p2]] = 1
                    else:
                        hash_table[s[p2]] += 1
                else:
                    return best
                

            else:
                hash_table[s[p1]] -= 1
                p1 += 1

        return best
                # update frequencies
            
            
            
            
            


        