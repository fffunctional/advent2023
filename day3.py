import math as m, re

board = list(open("day3.txt"))
rows, cols = len(board), len(board[0].rstrip("\n"))

chars = {(r, c): [] for r in range(rows)
                    for c in range(cols)
                    if board[r][c] not in '0123456789.'}
# Create a lookup table whose keys are the coordinates of symbols

for r, row in enumerate(board):
# For each row on the board
    for n in re.finditer(r'\d+', row):
    # For each Match of a number (consecutive digits)
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}
        # Make a list of the coordinates that make up the number's edge
        # i.e. anything that is up to one row above or below and up to
        # one character before or after the matched number

        for o in edge & chars.keys():
        # If an edge coordinate is the location of a symbol:
            chars[o].append(int(n.group()))
            # append the integer to that symbol's adjacency list

print(sum(sum(p) for p in chars.values()),
# for Part 1, just add up all the symbol-adjacent numbers
sum(m.prod(p) for p in chars.values() if len(p)==2))
# for Part 2, sum the products of gear-adjacent numbers;
# conveniently, all symbols with 2 adjacent numbers are gears
