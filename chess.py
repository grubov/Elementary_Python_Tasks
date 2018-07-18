def validation(n):
    try:
        number = int(n)
        if 80 > number > 0:
            return number
        else:
            raise ValueError
    except ValueError:
        print('Incorrect value, enter a number < 79 and > 0')
        return 0


def board_is_valid(w, h):
    if w and h:
        return True


class Board:
    """A board class"""

    def __init__(self, width, height):
        self.board = []
        self.width = width
        self.height = height

    def print(self):
        for i in range(self.height):
            self.board.append([])
            for j in range(self.width):
                if (i + j) % 2 == 0:
                    self.board[i].append('*')
                else:
                    self.board[i].append(' ')
        for row in self.board:
            print(' '.join(row))


if __name__ == "__main__":
    width_raw = input("width=")
    width = validation(width_raw)
    height_raw = input("height=")
    height = validation(height_raw)
    if board_is_valid(width, height):
        board = Board(width, height)
        board.
        print()
    else:
        print('Can\'t print a board, incorrect values')

""" Alternative print

for row in board:
   for elem in row:
       print(elem, end = ' ')
   print()
   
"""
