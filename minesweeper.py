import random
import re

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
                if (r,c) in self.dug: # check to see if it's already there ...
                    continue # ... don't dig where you've already dug.
                # another implicit 'else' here ...
                self.dig(r,c) # ... if that (r,c) tuple is *not* dug into, then go ahead and do so.
        # not sure what return True achieves here--jsut confirmation that the method completely executed ...?
        return True
        # overall insight: we should never actually hit a bomb; we should always be stopping right before one.

    #def __str__(self):
        # a "magic function" where it prints out whatever the object returns.
        # we can use this to return a string that shows the board.
        
        # create a new array that represents what the user should see:
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]  # create a list of sublists, both of dim_size
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:  # if that (row, col) is in self.dig (i.e., has already been dug) ...
                    visible_board[row][col] = str(self.board[row][col]) # ... we put self.board value into visible_board
                # if it's NOT already dug, then we'll make it a space, because we don't want the
                # user to see the information it contains.
                else:
                    visible_board[row][col] = ' '
        # put this entire board representation into a string
        # string_rep = ''
        # we could go into spectacular code to make it look better, but she felt correctly that getting it to work is more important


def play(dim_size=10, num_bombs=10):
    # create board and plant bombs
    board = Board(dim_size, num_bombs)

    # show the user the board and ask them for input

    # if location is a bomb, the game ends
    # if not, dig recurvsively until until the spot is next to a bomb
    # rinse/repeat until there are no more spots to dig

    safe = True # because we haven't dug anywhere yet

    while len(board.dug) < board.dim_size ** 2 - num_bombs: # meaning that they still have places to play
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row, col:  "))
        # the above basically says "match anything that is a comma with a space."
        # this makes handling different combinations of spaces and characters easier.
        # this tells us where the user is trying to dig
        row, col = int(user_input[0]), int(user_input[-1])
        # did not understand the explanation for why -1 may be suitable.
        # the below helps to keep us in bounds:
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid spot. Try again")
            continue
        # if it's valid, we dig at that location, so we invoke board.dig()
        # we can use this to tell us if we have uncovered a bomb.
        safe = board.dig(row,col) # naturally, we start out as "safe"; we haven't dug up any bombs
        if not safe: #meaning, we dug up bomb ...
            break # ... as in, game over. This removes us from the while loop.

    # we could exit the while loop only because we won or lost; no other possibilities
    # we dug in every possible spot to dig and didn't hit any bombs.
    if safe: # "still safe after everything"
        print ("Congratulations!!")
    else: # that, or you lost.
        print("Sorry; game over!!")
        # to show the entire board.
        # Don't understand where board.dug is coming from
        # (see the Board class initialization at the top.)
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__': # this is just a way of making sure you run this particular file if you have dependent files
    play()
