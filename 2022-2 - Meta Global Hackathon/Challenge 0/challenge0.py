# Meta Global Hackathon 2022
# Eric K.

# Open file
rollercoasters = []
with open("rollercoasters_medium_input.txt", "r") as f:
    for line in f:
        rollercoasters.append(int(line))


# Find the longest ascending subsequence
def longest_ascending_subsequence(rollercoasters):
    if len(rollercoasters) == 0:
        return 0
    if len(rollercoasters) == 1:
        return 1
    max_length = 1
    for i in range(len(rollercoasters)):
        length = 1
        for j in range(i + 1, len(rollercoasters)):
            if rollercoasters[j] > rollercoasters[j - 1]:
                length += 1
            else:
                break
        if length > max_length:
            max_length = length
    return max_length


# Output to file
with open("rollercoasters_out.txt", "w") as f:
    f.write(str(longest_ascending_subsequence(rollercoasters) * 10))
