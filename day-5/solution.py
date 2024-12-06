import functools
from collections import defaultdict

def read_data(input):
    rules = defaultdict(set)
    print_orders = []
    with open(input, "r") as f:
        rule = True
        for line in f.readlines():
            line = line.strip()

            # Once we hit a blank line 
            # we are done with rules
            if not line:
                rule = False
                continue

            if rule:
                before, after = line.split("|")
                rules[int(after)].add(int(before))
            else:
                pages = [int(x) for x in line.split(",")]
                print_orders.append(pages)
    return (rules, print_orders)


def check_valid_orders(rules, orders):
    valid_orders = []
    invalid_orders = []
    for order in orders:
        disallowed_pages = set()
        valid = True
        for page in order:
            if page in disallowed_pages:
                valid = False
                break
            disallowed_pages.update(rules[page])
        if valid:
            valid_orders.append(order)
        else:
            invalid_orders.append(order)
    return valid_orders, invalid_orders


def get_middle_page_sum(valid_orders):
    sum = 0
    for order in valid_orders:
        assert len(order) % 2 != 0, "Where is the middle"
        middle_index = len(order) // 2
        sum += order[middle_index]
    return sum


def part_1():
    rules, print_orders = read_data("input.txt")
    valid_orders, _ = check_valid_orders(rules, print_orders)
    part_1_result = get_middle_page_sum(valid_orders)
    print(f"Part 1 result = {part_1_result}")


def fix_orders(invalid_orders, rules):
    def compare(page1, page2):
        if page2 in rules[page1]:
            return 1
        elif page1 in rules[page2]:
            return -1
        else:
            return 0
    fixed_orders = []
    for order in invalid_orders:
        fixed_orders.append(
            sorted(order, key=functools.cmp_to_key(compare)))
    return fixed_orders


def part_2():
    rules, print_orders = read_data("input.txt")
    _, invalid_orders = check_valid_orders(rules, print_orders)
    fixed_orders = fix_orders(invalid_orders, rules)
    part_2_result = get_middle_page_sum(fixed_orders)
    print(f"Part 2 result = {part_2_result}")
    

part_1()
part_2()
