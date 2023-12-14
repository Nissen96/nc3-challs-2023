from random import choice

with open("flag.txt") as f:
    flag = f.read().strip()

assert all(c in "NC3{_abcdefghijklmnopqrstuvwxyz}" for c in flag)

result = 0
for c in flag.encode():
    if choice((0, 1)) == 0:
        result += c
    else:
        result *= c

print(result)
