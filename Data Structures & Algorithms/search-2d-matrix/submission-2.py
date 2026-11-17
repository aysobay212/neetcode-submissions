class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first we want to find the target row
        # we can start at the bottom row, check the first value to see if its < the target
        found = None

    
        l = 0
        r = len(matrix) - 1
        # find the row in the matrix
        while l <= r:
            m = l + (r-l)//2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        found = matrix[r]
        if r < 0:
            return False

        l = 0
        r = len(found) - 1
        while l <= r:
            m = l + (r-l)//2
            if found[m] == target:
                return True
            elif found[m] < target:
                l = m + 1
            else:
                r = m - 1 
        return False

        # simple binary search
                
        