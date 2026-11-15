class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # non-duplicacy for rows        
        for row in board:
            nonempty_row = []
            for num in row:
                if num.isdigit():
                    nonempty_row.append(num)
            new_row = set(nonempty_row)
            if len(new_row) < len(nonempty_row):
                return False
                
        # NOTE:　merge the row/column non-duplicacy for loops
        # non-duplicacy for columns (j), rows (i)
        subbox = [[] for _ in range(9)]
        for i in range(0, 9, 1):
            nonempty_column = []
            
            for j in range(0, 9, 1):
                if board[j][i].isdigit():
                    nonempty_column.append(board[j][i])

                    box_index = (i // 3) * 3 + (j // 3)
                    subbox[box_index].append(board[j][i])

            new_column = set(nonempty_column)
            if len(new_column) < len(nonempty_column):
                return False
        
        # non-duplicacy for 3x3 sub-boxes  
        for grid in subbox:
            set_grid = set(grid)
            if len(set_grid) < len(grid):
                return False
        
        return True

       
 

        