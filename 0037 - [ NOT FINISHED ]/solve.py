done,prev=0,-1

def printpos(pos):
    for i in pos:
        print(f"{i} = [{i//9}][{i%9}] = {pos[i]}")


def deletepos(pos):
    for i in pos:
        if len(pos[i])==1:
            print(f"[{i//9}][{i%9}]")

board = [[".",".","9","7","4","8",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         [".","2",".","1",".","9",".",".","."],
         [".",".","7",".",".",".","2","4","."],
         [".","6","4",".","1",".","5","9","."],
         [".","9","8",".",".",".","3",".","."],
         [".",".",".","8",".","3",".","2","."],
         [".",".",".",".",".",".",".",".","6"],
         [".",".",".","2","7","5","9",".","."]]

b = [['.', '.', '9', '7', '4', '8', '.', '.', '2'], 
         ['7', '.', '.', '6', '.', '2', '.', '.', '9'], 
         ['.', '2', '.', '1', '.', '9', '.', '.', '.'], 
         ['.', '.', '7', '9', '8', '6', '2', '4', '1'], 
         ['2', '6', '4', '3', '1', '7', '5', '9', '8'], 
         ['1', '9', '8', '5', '2', '4', '3', '6', '7'], 
         ['9', '.', '.', '8', '6', '3', '.', '2', '.'], 
         ['.', '.', '2', '4', '9', '1', '.', '.', '6'], 
         ['.', '.', '.', '2', '7', '5', '9', '.', '.']]

pos = {i:[j for j in range(1,10)] if board[i//9][i%9]=='.' else [int(board[i//9][i%9])] for i in range(81)}

while done!=prev and done<81:
    prev = done
    done=0
    for i in range(81):
        if board[i//9][i%9]==".":
            for j in range(9):
                # REMOVE POSSIBILITIES IN THE SAME ROW
                if board[i//9][j]!='.' and int(board[i//9][j]) in pos[i]:
                    pos[i].remove(int(board[i//9][j]))

                # REMOVE POSSIBILITIES IN THE SAME COLUMN
                if board[j][i%9] != '.' and int(board[j][i%9]) in pos[i]:
                    pos[i].remove(int(board[j][i%9]))

                # REMOVE POSSIBILITIES IN THE SAME BOX
                r = (i//27*3)+(j//3)
                c =(i%9)//3*3+(j%3)
                if board[r][c]!='.' and int(board[r][c]) in pos[i]:
                    pos[i].remove(int(board[r][c]))

            if len(pos[i])==1:
                board[i//9][i%9] = str(pos[i][0])
                done+=1
        else:
            done+=1
    print(done)

# complete the rest
# THE IDEA: WHEN ONLY ONE CELL HAS ONEE POS IN THE ROW OR COLUMN OR BOX
if done!=81:
    for i in range(9):
        row = [item for arr in list(pos.values())[i*9:(i+1)*9] for item in arr]
        column = [item for key, arr in pos.items() if key % 9 == i and len(pos[i])!=1 for item in arr]

        for j in range(1,10):
            if row.count(j)==1:
                print(f"row {i} with number {j}")

            if column.count(j)==1:
                print(f"col {i} with number {j}")