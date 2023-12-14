from pwn import server
import random


with open("flag.txt") as f:
    FLAG = f.read().strip()


def send_letter(conn):
    idx = random.randrange(0, len(FLAG))
    conn.sendline(b"#" * len(FLAG))
    conn.sendline(b" " * idx + FLAG[idx].encode() + b" " * (len(FLAG) - idx - 1))
    conn.sendline(b"#" * len(FLAG))
    conn.close()


if __name__ == "__main__":
    s = server(6346, callback=send_letter)
    print("Waiting for connections...")
    while True:
        s.next_connection()
