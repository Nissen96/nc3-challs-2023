import random


with open("flag.txt", "rb") as f:
    FLAG = f.read().strip()


def push_int(n):
    ops = ["PUSH"]
    for b in bin(n)[2:]:
        ops.append("DBL")
        if b == "1":
            ops.append("INC")
    return ops


# Generate random a and b values and encode each flag char
params = []
for y in FLAG:
    a = random.randint(0x00, 0xff)
    b = y ^ a
    params.append((a, b))

"""
Program:

print prompt
read input
for each input char:
    decode char with a and b
    if result is zero:
        char matched flag, pop next
    else:
        jump to currently unspecified address (insert HAHA cycle later)
entire flag correct, print welcome message
exit
"""

ops = [f"PUTC {ord('>')}", f"PUTC {ord(' ')}"]
ops.append(f"READ {len(FLAG)}  # Read flag")
for a, b in params[::-1]:
    ops.extend(push_int(a))
    ops.append("XOR")
    ops.append("POP")
    ops.extend(push_int(b))
    ops.append("SUB")
    ops.append("POP")
    ops.append("JNZ")
    ops.append("POP")

for c in "🎅 Korrekt! Velkommen ind 🎅\n".encode():
    ops.append(f"PUTC {c}")
ops.append("EXIT")

print("\n".join(ops))
