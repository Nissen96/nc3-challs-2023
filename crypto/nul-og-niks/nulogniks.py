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


def main():
    print("Velkommen til Kryptonissens Krypteringsservice!")
    key = secrets.token_bytes(len(flag))

    while True:
        print("Muligheder:")
        print("1) Krypter besked")
        print("2) Krypter flag")
        print("3) Afslut")

        choice = input("> ")
        if choice == "1":
            msg = input("Besked: ").encode()
            enc_msg = encrypt(msg, key)
            print(enc_msg.hex())
        elif choice == "2":
            enc_flag = encrypt(flag, key)
            print(enc_flag.hex())
        elif choice == "3":
            return
        else:
            print("Hov hov, det ka du ik")
        print()


if __name__ == "__main__":
    main()
