from IPython.display import clear_output

def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    print('[' + board[4]    + '   ' +   board[9]   +  '   '   +   board[2] + ']')
    print('[' + board[3]    + '   ' +   board[5]   +  '   '   +   board[7] + ']')
    print('[' + board[8]    + '   ' +   board[1]   +  '   '   +   board[6] + ']')
 