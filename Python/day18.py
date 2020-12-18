# Nyveon
# Advent of code 2020
# Day 18
# Python 3

# -- Input --
file = open("day18_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()[:-1]
file.close()
lines = file_in.split("\n")
for i in range(len(lines)):
    lines[i] = lines[i].replace(" ", "")


# -- Part 1 --

operations = {"+" : (lambda x,y: x+y), "*" : (lambda x,y: x*y) }

def evaluate_all(lines):
    sum = 0
    for i in lines:
        sum += Equation_tree(i).evaluate()
    return sum

class Node_internal:
    def __init__(self, left, info, right):
        self.left = left
        self.info = info
        self.right = right

    def evaluate(self):
        return operations[self.info](self.left.evaluate(), self.right.evaluate())

class Node_external:
    def __init__(self, info):
        self.info = info

    def evaluate(self):
        return int(self.info)

class Equation_tree:
    def __init__(self, equation):
        global k
        global s
        s = equation + ";"
        k = 0

        def expression():
            global k
            global s
            a = final()
            while s[k] == "+" or s[k] == "*":
                op = s[k]
                k += 1
                b = final()
                a = Node_internal(a, op, b)
            return a

        def final():
            global k
            global s
            if s[k].isalpha() or s[k].isdigit():
                a = Node_external(s[k])
                k += 1
                return a
            if s[k] == "(":
                k += 1
                a = expression()
                k += 1
                return a
            assert False

        a = expression()
        self.root = a

    def evaluate(self):
      return self.root.evaluate()


print("Part 1:", evaluate_all(lines), 2743012121210)

# -- Part 2 --

# Re-define

class Equation_tree:
    def __init__(self, equation):
        global k
        global s
        s = equation + ";"
        k = 0

        def expression():
            global k
            global s
            a = factor()
            while s[k] == "*":
                op = s[k]
                k += 1
                b = factor()
                a = Node_internal(a, op, b)
            return a

        def factor():
            global k
            global s
            a = final()
            while s[k] == "+":
                op = s[k]
                k += 1
                b = final()
                a = Node_internal(a, op, b)
            return a

        def final():
            global k
            global s
            if s[k].isalpha() or s[k].isdigit():
                a = Node_external(s[k])
                k += 1
                return a
            if s[k] == "(":
                k += 1
                a = expression()
                k += 1
                return a
            assert False

        a = expression()
        self.root = a

    def evaluate(self):
      return self.root.evaluate()


print("Part 2:", evaluate_all(lines), "65658760783597")