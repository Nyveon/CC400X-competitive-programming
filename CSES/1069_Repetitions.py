# Eric K
# 20/03/2023

sequence = input()
current_character = sequence[0]
counter = 0
max_counter = 0

for character in sequence:
    if character == current_character:
        counter += 1
        if counter > max_counter:
            max_counter = counter
    else:
        counter = 1
        current_character = character

print(max_counter)
