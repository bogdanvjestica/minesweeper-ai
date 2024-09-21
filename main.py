import random


class Minesweeper:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = self.generate_board()

    def generate_board(self):
        board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        mine_count = 0

        while mine_count < self.mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if board[y][x] != -1:
                board[y][x] = -1
                mine_count += 1
                self.update_neighbors(board, x, y)
        return board

    def update_neighbors(self, board, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.width and 0 <= y + j < self.height and board[y + j][x + i] != -1:
                    board[y + j][x + i] += 1

    def display(self):
        for row in self.board:
            print('\t'.join(str(cell) for cell in row))


field = Minesweeper(10, 10, 10)
field.display()
