INPUT_FILENAME = "input.txt"
DIRECTIONS = [">", "v", "<", "^"]

def load_data(filename):
    with open(filename, "r") as f:
        map = []
        start = (-1, -1)
        for row, line in enumerate(f.readlines()):
            line = line.strip()
            mapline = []
            for col, char in enumerate(line):
                if char in DIRECTIONS:
                    start = (row, col)
                mapline.append(char)
            map.append(mapline)
        return map, start

def count_positions(map, start):
    m = len(map)
    n = len(map[0])
    curr = start
    positions = set()
    while True:
        positions.add(curr)
        char = map[curr[0]][curr[1]]
        if char == ">":
            next = (curr[0], curr[1] + 1)
        elif char == "v":   
            next = (curr[0] + 1, curr[1])
        elif char == "<":
            next = (curr[0], curr[1] - 1)
        else:   # char == ^
            next = (curr[0] - 1, curr[1])
            
        if not (m > next[0] >= 0 and n > next[1] >= 0):
            return len(positions)
        next_char = map[next[0]][next[1]] 
        if next_char == "#":
            map[curr[0]][curr[1]] = rotate_90(map[curr[0]][curr[1]])
        else:
            map[curr[0]][curr[1]] = "."
            map[next[0]][next[1]] = char
            curr = next


def rotate_90(char):
    # Possible directions, turning 90 each time
    assert char in DIRECTIONS
    idx = DIRECTIONS.index(char)
    # Return the next direction in order
    return DIRECTIONS[(idx + 1) % len(DIRECTIONS)]


map, start = load_data(INPUT_FILENAME)
print(count_positions(map, start))
