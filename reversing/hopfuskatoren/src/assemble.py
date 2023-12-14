import random
import struct
import sys


def encode(ops):
    opcodes = []
    for op in ops:
        if "#" in op:
            op = op[:op.find("#")]

        match op.upper().split():
            case ["PUSH"]:
                opcodes.append(b"\x00")
            case ["POP"]:
                opcodes.append(b"\x01")
            case ["INC"]:
                opcodes.append(b"\x02")
            case ["DBL"]:
                opcodes.append(b"\x03")
            case ["SUB"]:
                opcodes.append(b"\x04")
            case ["XOR"]:
                opcodes.append(b"\x05")
            case ["JNZ", n]:
                opcodes.append(b"\x06" + struct.pack("<H", int(n)))
            case ["JNZ"]:
                # JNZ with no jump val
                opcodes.append(b"\x06\x00\x00")
            case ["READ", n]:
                opcodes.append(b"\x07" + bytes([int(n)]))
            case ["WRITE", n]:
                opcodes.append(b"\x08" + bytes([int(n)]))
            case ["PUTC", c]:
                opcodes.append(b"\x09" + bytes([int(c)]))
            case ["EXIT"]:
                opcodes.append(b"\x7f")
            case _:
                print(f"Nope: {op}")
    return opcodes


def obfuscate(ops):
    n = len(ops)
    error = "HA".encode()
    m = len(error) * 7 + 3

    # Initialize 20x size bytecode area randomly
    bytecode = [random.randint(0x00, 0xff) for _ in range(n * 20)]

    # Choose random indices within area for actual opcodes
    i = random.randint(m + 3, 0xff)
    indices = [i]
    for _ in range(n - 1):
        i += random.randint(15, 25)
        if i > len(bytecode) - 5:
            return obfuscate(ops)
        indices.append(i)

    # Find now filled ranges
    used = set()
    for i in indices:
        used |= set(range(i, i + 5))

    # Shuffle operand order and insert jumps to the next op
    random.shuffle(indices)
    indices.append(len(bytecode))
    for op, i, j in zip(ops, indices, indices[1:]):
        bytecode[i:i + len(op) + 2] = op + struct.pack("<h", j - i - len(op))

    # Set entrypoint to address of first operand
    bytecode[:2] = struct.pack("<h", indices[0])

    # Find unused space for infinite HAHA cycle
    cycle_indices = []
    i = 3
    while i < len(bytecode):
        if any(i + j in used for j in range(m)):
            i += 1
            continue
        cycle_indices.append(i)
        i += m

    # Insert cycle - each entry:
    #   prints "H"
    #   randomly chosen instruction
    #   prints "A"
    #   randomly chosen instruction
    #   randomly chosen instruction
    #   jump to next entry in cycle
    random.shuffle(cycle_indices)
    cycle_indices.append(cycle_indices[0])
    for i, j in zip(cycle_indices, cycle_indices[1:]):
        jank = b""
        for c in error:
            jank += bytes([9, c, 2, 0, random.choice(b"\x02\x03\x04\x05"), 2, 0])
        jank += bytes([random.choice(b"\x02\x03\x04\x05")])
        assert m == len(jank) + 2
        bytecode[i:i + m] = jank + struct.pack("<h", j - i - (m - 2))

    # Ensure empty JNZ jumps end in the cycle immediately
    for op, i in zip(ops, indices):
        if op == b"\x06\x00\x00":
            cycle_val = random.choice(cycle_indices)
            bytecode[i + 1:i + 3] = struct.pack("<h", cycle_val - i - 1)

    return bytes(bytecode)


def main():
    with open(sys.argv[1]) as f:
        ops = f.read().strip().split("\n")

    opcodes = encode(ops)
    bytecode = obfuscate(opcodes)

    with open("prog", "wb") as f:
        f.write(bytecode)


if __name__ == "__main__":
    main()
