import sys

for line in sys.stdin:
    for char in line:
        if char.isdigit():
            print(char, end='')
    print()
