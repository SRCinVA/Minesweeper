import random

class Board:    # this creates the board object
    def __init__(self, dim_size, num_bombs):  
        # need to track these parameters:
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board, first with a helper function:
        self.board = self.make_new_board() # this will enable us to plant the bombs
        # my understanding on why we're doing this ... is not clear
        self.assign_values_to_board()

        # intialize a set to keep track of which locations have been uncovered.
        # (this will be in tuples of row, column)

        self.dug = set()

    def assign_values_to_board(self):
        # !?!?! with bombs planted, assign a number of 0-8 to all empty spaces,
        # which indicates how many neighboring bombs there are. (How will this help us ... ?)
        for r in range(self.dim_size):
            

    def make_new_board(self):   # using dim size and num_bombs, make a new board
                                # in the form of a list of lists (good for a 2d structure)
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # it will be a square, so both of those blanks will be the same number
        # (seems to be columns and then rows.)

        # plant the bombs:
        bombs_planted = 0
        while bombs_planted < self.num_bombs: # we're doing something unbounded, so a while loop is better
            loc = random.randint(0, self.dim_size**2 - 1) # **2 to square it; - 1 so that it encompasses the highest index.
            row = loc // self.dim_size  # don't understand this. (Space 22 is not in row 4.)
            col = loc % self.dim_size # don't understand this one, either

            if board[row][col] == '*': # if that spot equals a bomb (the star), then we've alrady planted one.
                continue # meaning, just keep going on

            board[row][col] = '*'
            bombs_planted += 1
        # when all of this is done, return the board:
        return board

def play(dim_size=10, num_bombs=10):
    # create board and plant bombs
    # show the user the board and ak them for input
    # if location is a bomb, the game ends
    # if not, dig recurvsively until until the spot is next to a bomb
    # rinse/repeat until there are no more spots to dig

    pass

