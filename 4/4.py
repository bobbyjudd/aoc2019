"""
--- Day 4: Secure Container ---

You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet these criteria?

--- Part Two ---

An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

    112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
    123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
    111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).

How many different passwords within the range given in your puzzle input meet all of the criteria?

"""
def digits_ascending(num):
    num_s = str(num)
    for i in range(1,len(num_s)):
        if int(num_s[i-1]) > int(num_s[i]):
            return False
    return True

def two_adjacent(num):
    num_s = str(num)
    for i in range(1,len(num_s)):
        if num_s[i-1] == num_s[i]:
            return True
    return False

def total_pw_count(input_range, pt_2=False):
    count = 0
    for key in input_range:
        if digits_ascending(key) and two_adjacent(key)):
                count += 1
    return count

def part_2(input_range):
    # Solution from https://www.reddit.com/r/adventofcode/comments/e5u5fv/2019_day_4_solutions/f9mdg1t/
    def check(n):
        return list(n) == sorted(n) and 2 in map(n.count, n)
    return sum(check(str(n)) for n in input_range)

if __name__ == "__main__":
    # Range 235741-706948
    range_start, range_stop = 235741, 706948
    print('Part 1: {}'.format(total_pw_count(range(range_start, range_stop+1))))
    print('Part 2: {}'.format(part_2(range(range_start, range_stop+1))))