import numpy as np

class Minesweeper:
    def __init__(self, height: int=5, width: int=5, percent_mines=0.15):
        self.height = height
        self.width = width
        self.percent_mines = percent_mines

    def createBoard(self):
        board = np.random.uniform(0, 1, (self.height, self.width))
        board = (board < self.percent_mines).astype("int8")
        self.num_bombs = np.sum(board)
        board = np.pad(board, (1,1), constant_values=(0,0))

        self.ans_board = np.zeros((self.height, self.width))
        for idx in range(len(self.ans_board)):
            for idy in range(len(self.ans_board[0])):
                if board[idx+1, idy+1] != 1:
                    self.ans_board[idx, idy] = np.sum(board[idx:idx+3, idy:idy+3])
                else:
                    self.ans_board[idx, idy] = -1

    def createMask(self):
        self.mask = np.zeros((self.height, self.width))

    def displayBoard(self):
        showBoard = np.zeros((self.mask.shape))
        showBoard = showBoard.tolist()

        for idx in range(len(self.mask)):
            for idy in range(len(self.mask[0])):
                showBoard[idx][idy] = " " if self.mask[idx, idy]==0 else ("💣" if int(self.ans_board[idx, idy]) == -1 else int(self.ans_board[idx, idy]))
        return showBoard

    def updateMask(self, ans_board, mask, x, y):
        if ((x<0) or (y<0) or (x>self.height-1) or (y>self.width-1)):
            return # same as return None

        if mask[x, y] == 1:
            return

        if ans_board[x, y] > 0:
            mask[x, y] = 1
            return

        if ans_board[x, y] == 0:
            mask[x, y] = 1
            self.updateMask(ans_board, mask, x-1, y)
            self.updateMask(ans_board, mask, x+1, y)
            self.updateMask(ans_board, mask, x, y-1)
            self.updateMask(ans_board, mask, x, y+1)
            return

    def isOnBomb(self, x, y):
        if self.ans_board[x, y] == -1:
            return True
        return False

    def isWon(self):
        if np.sum(self.mask) == (self.height*self.width - self.num_bombs):
            return True
        return False
