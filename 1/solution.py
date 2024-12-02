from collections import Counter

left_array = []
right_array = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        left, right = line.split('   ')
        left_array.append(int(left.strip()))
        right_array.append(int(right.strip()))

left_array.sort()
right_array.sort()
# print(left_array)
# print(right_array)

assert (len(left_array) == len(right_array)), "Should recieve even len lists"
numbers = len(left_array)


# Part 1: Sum the total distances in the list 
total = 0
for i in range(numbers):
    left = left_array[i]
    right = right_array[i]
    dist = abs(left - right)
    total += dist

print(f"Part 1 result = {total}")


# Part 2: Similarity score

left_counts = Counter(left_array)
right_counts = Counter(right_array)

sim_score = 0
for num in left_array:
    sim_score += num * right_counts[num]

print(f"Part 2 result = {sim_score}")
    

