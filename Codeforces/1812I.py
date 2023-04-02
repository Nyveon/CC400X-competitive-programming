# TRIED:
# YES/YES
# YES/NO
# NO/NO
# NO/YES

x = "NO"
y = "YES"

a = ["YES", "NO", "YES", "YES", "YES", "NO", "YES", "NO", "YES", "YES", "YES",
     "YES", "YES", "YES", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "NO", "NO", x, y]

t = int(input())

for i in range(t):
    print(a[i])
