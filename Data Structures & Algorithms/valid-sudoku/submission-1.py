class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # look at rows
        for row in board:
            hashset = set()
            for value in row:
                if value not in hashset:
                    if value != ".": # ignore empty cells
                        hashset.add(value)
                else:
                    return False

        # look at columns
        for i in range(0, len(board)):
            hashset = set()
            for j in range(0, len(board)):
                value = board[j][i]
                if value not in hashset:
                    if value != ".": # ignore empty cells
                        hashset.add(value)
                else:
                    return False      

        # check for 3x3 squares
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                hashset = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        value = board[i][j]
                        if value != ".":
                            if value in hashset:
                                return False
                            hashset.add(value)

        return True