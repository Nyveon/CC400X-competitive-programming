# Nyveon
# Advent of code 2020
# Day 8
# Python 3

# -- Input --
file = open("day8_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()
file.close()
lines = file_in.split("\n")
lines.pop()


# -- Main function --
def interpret(lines):
    pointer = 0
    accumulator = 0
    visited = []

    while pointer < len(lines):
        if pointer in visited:
            return (False, accumulator) # stuck
        else:
            visited.append(pointer)
        instruction = lines[pointer][:3]
        value = int(lines[pointer][4:])
        if instruction == "acc":
            accumulator += value
            pointer += 1
        elif instruction == "jmp":
            pointer += value
        elif instruction == "nop":
            pointer += 1

    return (True, accumulator) # end


# -- Part 1 --

print("Part 1: ", interpret(lines)[1])


# -- Part 2 --

for i in range(0, len(lines)):
    if lines[i][0] == "j":
        mod_lines = lines.copy()
        mod_lines[i] = "nop " + lines[i][4:]
        ans = interpret(mod_lines)
        if ans[0]:
            break

print("Part 2: ", ans[1])