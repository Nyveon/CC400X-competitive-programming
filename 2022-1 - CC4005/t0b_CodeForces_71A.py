# Nyveon
# T0 CC4005
# Problem B - Palabras muy largas


inputs = int(input())
for i in range(inputs):
    word = input()

    if len(word) > 10:
        print(f"{word[0]}{len(word)-2}{word[-1]}")
    else:
        print(word)
