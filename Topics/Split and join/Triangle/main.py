height = int(input())

for i in range(1, height + 1):
    print(" " * (height - i), end="")
    print("#" * (i * 2 - 1))
