from pwn import server
from random import choice

with open("flag.txt", "rb") as f:
    flag = f.read().strip()

def calculate(conn):
    result = 0
    for c in flag:
        if choice((0, 1)) == 0:
            result += c
        else:
            result *= c

    conn.sendline(str(result).encode())
    conn.close()


if __name__ == "__main__":
    s = server(22413, callback=calculate)
    print("Waiting for connections...")
    while True:
        s.next_connection()
