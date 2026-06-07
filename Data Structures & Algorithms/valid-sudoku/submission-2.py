class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colmap = {}
        rowmap = {}
        col3x3map = {}
        dim = len(board)
        for row in range(0,dim):
            for col in range(0,dim):
                if board[row][col] == ".":
                    continue

                idx3 = "r"+str(row//3)+"c"+str(col//3)
                if idx3 not in col3x3map:
                    col3x3map[idx3] = []
                
                val = board[row][col]
                if val in col3x3map[idx3]:
                    return False
                
                col3x3map[idx3].append(val)

                if col not in colmap:
                    colmap[col]= []
                if row not in rowmap:
                    rowmap[row]= []
                
                if val in colmap[col]:
                    return False
                if val in rowmap[row]:
                    return False
                
                colmap[col].append(val)
                rowmap[row].append(val)
        
        return True

                


                


