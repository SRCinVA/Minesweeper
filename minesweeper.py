class Board:    # this creates the board object
    def __init__(self, dim_size, num_bombs):  
        # need to track these parameters:
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board, first with a helper function:
        self.board = self.make_new_board() # this will enable us to plant the bombs


        # intialize a set to keep track of which locations have been uncovered.
        # (this will be in tuples of row, column)

        self.dug = set()

    def make_new_board(self):   # using dim size and num_bombs, make a new board
                                # in the form of a list of lists (good for a 2d structure)
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # it will be a square, so both of those blanks will be the same number
        # (seems to be columns to rows.)

def play(dim_size=10, num_bombs=10):
    # create board and plant bombs
    # show the user the board and ak them for input
    # if location is a bomb, the game ends
    # if not, dig recurvsively until until the spot is next to a bomb
    # rinse/repeat until there are no more spots to dig

    pass

