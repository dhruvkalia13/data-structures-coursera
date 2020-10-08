# python3

from collections import namedtuple


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if opening_brackets_stack.__len__() == 0:
                opening_brackets_stack.append(Bracket(next, i))
                break
            item = opening_brackets_stack.pop()
            if not item.Match(next):
                opening_brackets_stack.append(Bracket(next, i))
                break
    if len(opening_brackets_stack) == 0:
        return 0
    else:
        return opening_brackets_stack.pop().position + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
