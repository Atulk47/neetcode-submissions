class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen1 = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen1:
                    return False
                seen1.add(board[i][j])

        for col in range(9):
            seen2 = set()
            for j in range(9):
                if board[j][col] == ".":
                    continue
                if board[j][col] in seen2:
                    return False
                seen2.add(board[j][col])


        for sq in range(9):
            see = set()
            for i in range(3):
                for j in range(3):
                    row = (sq//3)*3 + i
                    col = (sq%3)*3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in see:
                        return False
                    see.add(board[row][col])
        return True
            

        

        
        