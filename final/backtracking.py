n=int(input('Enter value of n : '))
#for board
board=[[0 for i in range(n)]for i in range(n)]
#for row in board:
 #print(row)
#for checking in previous columns
def check_columns(board,row,column):
 for i in range(row,-1,-1):
     if board[i][column]==1:
         return False
 return True
#for checking digonally
def check_diagonal(board,row,column):
  for i,j in zip(range(row,-1,-1),range(column,-1,-1)):
     if board[i][j]==1:
         return False
  for i,j in zip(range(row,-1,-1),range(column,n)):
     if board[i][j]==1:
         return False 
  return True
#backtracking
def nqn(board,row):
    if row==n:
     return True
    for i in range(n):
        if (check_columns(board,row,i)==True and check_diagonal(board,row,i)==True):
           board[row][i]=1
           if nqn(board,row+1):
               return True
           board[row][i]=0
    return False

nqn(board,0)
for row in board:
    print(row)