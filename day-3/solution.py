import re

with open("input.txt", "r") as f:
    mem = f.read()

matches = re.findall("mul\\(\\d*,\\d*\\)", mem)
tot = 0
for match in matches:
    left, right = match.split(",")
    left = left[4:]       # removes "mul("
    right = right[:-1]    # removes ")"
    tot += int(left) * int(right)
print(f"Part 1 result = {tot}")


# Part 2

tot = 0
do = True
while len(mem) > 0:

    # print(mem[:100], tot)

    next_mul = re.search("mul\\(\\d*,\\d*\\)", mem)
    next_dont = re.search("don't\\(\\)", mem)
    next_do = re.search("do\\(\\)", mem)

    # no more mul calls in the string
    if not next_mul:
        break
    
    # get the spans
    end = (len(mem), len(mem))
    next_mul = next_mul.span()
    next_dont = end if not next_dont else next_dont.span()
    next_do = end if not next_do else next_do.span()

    # print(next_mul)
    # print(next_dont)
    # print(next_do)

    # If we are not in an enabled section skip to the next do
    if not do:
        do = True
        mem = mem[next_do[1]:]
        continue

    # Check if the next don't() is before the next mul()
    if next_dont[0] < next_mul[0]:
        do = False
        mem = mem[next_dont[1]:]
        continue

    # Get the next mul() and add it to the total
    match = mem[next_mul[0]:next_mul[1]]
    left, right = match.split(",")
    left = left[4:]       # removes "mul("
    right = right[:-1]    # removes ")"
    tot += int(left) * int(right)
    mem = mem[next_mul[1]:]
    # print(match, int(left) * int(right), tot)

print(f"Part 2 result = {tot}")
