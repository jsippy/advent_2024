
# Load the data
puzzle = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        puzzle.append(line.strip())

def check_for_xmas(puzzle, row, col):
    tot = 0
    m = len(puzzle)
    n = len(puzzle)

    dirs = [-1, 0, 1]

    for row_dir in dirs:
        for col_dir in dirs:
            if row_dir == 0 and col_dir == 0:
                continue
            
            xmas = True
            for i, c in enumerate("XMAS"):
                curr_row = row + (row_dir * i)
                curr_col = col + (col_dir * i)
                 
                # Check if this index is in-bounds
                if curr_row < 0 or curr_row >= m:
                    xmas = False
                    break
                if curr_col < 0 or curr_col >= n:
                    xmas = False
                    break

                # Check if its the right letter
                if puzzle[curr_row][curr_col] != c:
                    xmas = False
                    break
            if xmas:
                tot += 1
    return tot


m = len(puzzle)
n = len(puzzle[0])

result = 0
for row in range(m):
    for col in range(n):
        
        # check for xmas
        if puzzle[row][col] != "X":
            continue
        
        # just gonna hardcode it
        result += check_for_xmas(puzzle, row, col)
print(f"Part 1 soultion = {result}")


# Part 2

def check_for_max_x(puzzle, row, col):
    assert puzzle[row][col] == "A"
    tot = 0
    m = len(puzzle)
    n = len(puzzle)

    # relative positions of the corners
    l = []
    positions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    l.append(zip(positions, "SSMM"))
    l.append(zip(positions, "SMSM"))
    l.append(zip(positions, "MMSS"))
    l.append(zip(positions, "MSMS"))

    for arrangement in l:
        found = True
        for pos, c in arrangement:
            curr_row = row + pos[0]
            curr_col = col + pos[1]
            if curr_row < 0 \
                    or curr_col < 0 \
                    or curr_row >= m \
                    or curr_col >= n \
                    or puzzle[curr_row][curr_col] != c:
                found = False
                break
        
        if found:
            # print(f"--- {(row, col)}")
            # print(f"{puzzle[row-1][col-1]} {puzzle[row-1][col+1]}")
            # print(f" {puzzle[row][col]} ")
            # print(f"{puzzle[row+1][col-1]} {puzzle[row+1][col+1]}")
            tot += 1
            
    return tot


result = 0
for row in range(m):
    for col in range(n):
        
        # check for mas-X
        if puzzle[row][col] != "A":
            continue
        
        # just gonna hardcode it
        result += check_for_max_x(puzzle, row, col)
print(f"Part 2 solution = {result}")






