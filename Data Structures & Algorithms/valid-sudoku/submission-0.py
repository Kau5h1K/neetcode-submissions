class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        sqrs = []

        row_len = len(board)
        col_len = len(board[0])
        sqrs_len = 9

        for i in range(row_len):
            seen = set()
            for j in range(row_len):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        for j in range(col_len):
            seen = set()
            for i in range(row_len):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        for sqr in range(sqrs_len):
            seen = set()
            for i in range(sqrs_len//3):
                for j in range(sqrs_len//3):
                    row = (sqr // 3) * 3 + i
                    col = (sqr % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True


        
        