def chk(table,a,b):
    for i in range(a-1,a+2):
        for j in range(b-1,b+2):
            if(i>=0 and i<len(table) and j>=0 and j<len(table) and table[i][j]!=1):
                table[i][j] = 2
    return table

def solution(board):
    cnt = 0
    size = len(board)
    for i in range(0,size):
        for j in range(0,size):
            if(board[i][j]==1):
                board = chk(board,i,j)
    print("부검",board)
    for i in range(0,size):
        for j in range(0,size):
            if board[i][j]==0:
                cnt = cnt + 1
    return cnt


ex = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
print(solution(ex))