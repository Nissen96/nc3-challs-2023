from pwn import server
import secrets


with open("flag.txt", "rb") as f:
    flag = f.read().strip()


def encrypt(pt, key):
    nonce = [secrets.randbelow(255) + 1 for _ in range(len(pt))]

    ct = [0]
    for i, (c, r) in enumerate(zip(pt, nonce)):
        k = key[i % len(key)]
        ct.append(c ^ k ^ r ^ ct[-1])

    return bytes(ct[1:])


def menu(conn):
    conn.sendline(b"Velkommen til Kryptonissens Krypteringsservice!")
    key = secrets.token_bytes(len(flag))

    while True:
        conn.sendline(b"Muligheder:")
        conn.sendline(b"1) Krypter besked")
        conn.sendline(b"2) Krypter flag")
        conn.sendline(b"3) Afslut")
        conn.send(b"> ")

        choice = conn.recvline().strip()
        if choice == b"1":
            conn.send(b"Besked: ")
            msg = conn.recvline().strip()
            enc_msg = encrypt(msg, key)
            conn.sendline(enc_msg.hex().encode())
        elif choice == b"2":
            enc_flag = encrypt(flag, key)
            conn.sendline(enc_flag.hex().encode())
        elif choice == b"3":
            conn.close()
            return
        else:
            conn.sendline(b"Hov hov, det ka du ik")
        conn.sendline()


if __name__ == "__main__":
    s = server(10101, callback=menu)
    print("Waiting for connections...")
    while True:
        s.next_connection()
