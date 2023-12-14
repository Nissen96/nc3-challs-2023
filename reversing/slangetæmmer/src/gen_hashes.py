import hashlib
import random

with open("flag.txt") as f:
    flag = f.read().strip()

for c in flag:
    a = hashlib.md5(c.encode()).hexdigest()
    b = hashlib.sha1(c.encode()).hexdigest()
    c = hashlib.sha256(c.encode()).hexdigest()
    hashes = [a, b, c]
    random.shuffle(hashes)
    print("".join(hashes))
