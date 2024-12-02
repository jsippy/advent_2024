def find_unsafe(row):
    if len(row) < 2:
        return None
    increasing = row[0] < row[1]
    for i in range(0, len(row) - 1):
        abs_diff = abs(row[i] - row[i + 1])
        if abs_diff < 1 or abs_diff > 3:
            return (i, i + 1)
        
        curr_direction = row[i] < row[i + 1]
        if increasing != curr_direction:
            return (i, i + 1)
    return None


def copy_and_remove(row, idx):
    copy = row.copy()
    del copy[idx]
    return copy

def load_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            data.append([int(x) for x in line.split(' ')])
    return data

def part1(data):
    part_1_result = 0
    for row in data:
        if not find_unsafe(row):
            part_1_result += 1
    print(f"Part 1 result = {part_1_result}")

def part2(data):
    part_2_result = 0
    for row in data:
        unsafe_idx = find_unsafe(row)

        # If there are no mistakes this row is safe
        if not unsafe_idx:
            part_2_result += 1
            continue

        # If there is only one mistake this row is safe
        # Try removing both numbers at the possible spot
        # Also try removing idx 0, since this could mess
        # up the whole direction
        idx1, idx2 = unsafe_idx
        if not find_unsafe(copy_and_remove(row, 0)):
            part_2_result += 1
            continue            
        if not find_unsafe(copy_and_remove(row, idx1)):
            part_2_result += 1
            continue            
        if not find_unsafe(copy_and_remove(row, idx2)):
            part_2_result += 1
            continue            
        print("Unsafe row:")
        print(row)
    print(f"Part 2 result = {part_2_result}")
    

if __name__ == "__main__":
    data = load_data("input.txt")
    part1(data)
    part2(data)
