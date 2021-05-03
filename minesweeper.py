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
        # with bombs planted, assign a number of 0-8 to all empty spaces (in all directions around that spot)
        # which indicates how many neighboring bombs there are.
        for r in range(self.dim_size):       # for row
            for c in range(self.dim_size):   # for column
                if self.board[r][c] == '*':  # if it's a bomb at that index ...
                    continue                 # ... 'continue' in order to not override any of the bombs already planted
                # this is an implicit 'else'
                # we use this function to populate 'self.board[r][c]'; showing how many bombs are in that [c][r] vicinity.
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)  
    # (just above) this function will give us the number of bombs in the area.          
    def get_num_neighboring_bombs(self, row, col):
        # now we have to iterate over every 9 spots surrounding every position.
        # also, don't go out of bounds.

        # initialize the total number to 0
        num_neighboring_bombs = 0
        # these two loops below will capture all surrouding directions of the 3*3 area
        for r in range(max(0,row-1), min(self.dim_size-1, row+1)+1):    # row-1 to catch index 0, row+1 to adjust it out of "index counting" 
                                            # and "+1" because range() in python is (bizarrely) exclusive of last item.
                                            # the max and min statments and their limits keep us in bounds when iterating.
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue # this is the original thing we were checking, so we just continue down the line
        return

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

    def dig(self, row, col):
        self.dug.add((row,col)) # this helps us be sure of where we've dug.

        if self.board[row][col] == '*': # return False if a bomb has been placed at that particular spot.
            return False
        # here's where it gets a bit more complicated
        elif self.board[row][col] > 0: # means we're near a bomb
            return True  # means we did not dig a bomb
        
        # if both of the above statements fail, then it's == 0
        
        # like get_num_of _Neiboring _bombs, we're going to employ the logic below to check the neighbors:

        # row-1 to catch index 0, row+1 to adjust it out of "index counting"
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                                            # and "+1" because range() in python is (bizarrely) exclusive of last item.
                                            # the max and min statments and their limits keep us in bounds when iterating.
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r,c) in self.dug:
                    continue # don't dig where you've already dug.
                self.dig(r,c) 

def play(dim_size=10, num_bombs=10):
    # create board and plant bombs
    board = Board(dim_size, num_bombs)

    # show the user the board and ask them for input


    # if location is a bomb, the game ends
    # if not, dig recurvsively until until the spot is next to a bomb
    # rinse/repeat until there are no more spots to dig

    pass

