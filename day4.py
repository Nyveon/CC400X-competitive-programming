# Nyveon
# Advent of code 2020
# Day 4
# Python 3

# -- Part 1 --

# Initialization
file = open("day4_input.txt", "r")
file_in = file.read()
file.close()
passports = file_in.split("\n\n")
part_1 = []

# Main loop
for item in passports:
    b = item.split()
    b.sort()
    s = ""

    for i in b:
        s += i[:3]

    if s == "byrcidecleyrhclhgtiyrpid":
        part_1.append(b)
    elif s == "byrecleyrhclhgtiyrpid":
        part_1.append(b)
        b.insert(1, "cid:-1")

# Output
print("Part 1:", len(part_1))


# -- Part 2 --


# Verification function. I NEED TO LEARN REGEX T_T
def verify(a):
    if 1920 <= int(a[0][4:]) <= 2002:  # byr
        if 2010 <= int(a[6][4:]) <= 2020:  # iyr
            if 2020 <= int(a[3][4:]) <= 2030:  # eyr
                if a[5][-2:] == "cm":
                    left = 150
                    right = 193
                elif a[5][-2:] == "in":
                    left = 59
                    right = 76
                else:
                    return False
                if left <= int(a[5][4:len(a[5])-2]) <= right:  # hgt
                    if a[4][4] == "#" and len(a[4]) == 11:  # hcl maybe add length check
                        if a[2][4:] in "ambblubrngrygrnhzloth":  # ecl
                            if len(a[7][4:]) == 9:  # pid
                                return True
    return False


# Main loop
count = 0
for item in part_1:
    flag = True
    if verify(item):
        count += 1

# Output
print("Part 2:", count)
