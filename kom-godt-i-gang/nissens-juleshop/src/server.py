from pwn import server


ITEMS = [("Julelys", 85), ("Gavepapir", 40), ("Sneskovl", 230), ("Juletræ", 760), ("Flag", 1_000_000)]

with open("flag.txt", "rb") as f:
    FLAG = f.read().strip()


def juleshop(conn, julesne=1000):
    conn.sendline(f"Du har i øjeblikket {julesne} JULESNE på din konto".encode())
    conn.sendline("Hvad vil du købe?".encode())
    for i, (item, price) in enumerate(ITEMS):
        conn.sendline(f"\t{i + 1}) {item} ({price} JULESNE)".encode())
    conn.send(b"> ")

    try:
        choice, price = ITEMS[int(conn.recvline().strip()) - 1]
        if price > julesne:
            conn.sendline(f"Den går ikke, du har ikke engang råd til 1x {choice}\n".encode())
            return juleshop(conn, julesne)

        if choice == "Flag":
            conn.sendline(f"Du har købt flaget for {price} JULESNE:".encode())
            conn.sendline(FLAG)
            return

        conn.sendline("Hvor mange vil du købe?".encode())
        conn.send(b"> ")
        amount = int(conn.recvline())
    except ValueError:
        conn.sendline(b"Hov hov, det var vist ikke et gyldigt valg!")
        return juleshop(conn, julesne)

    total = amount * price
    if total <= julesne:
        julesne -= total
        conn.sendline(f"Du har købt {amount} stk. {choice} for i alt {total} JULESNE".encode())
    else:
        conn.sendline(f"{total} JULESNE? Det har du altså ikke råd til!".encode())

    conn.sendline()

    return juleshop(conn, julesne)


def handler(conn):
    conn.sendline(b"Velkommen til Nissens Juleshop!\n")
    juleshop(conn)
    conn.close()


if __name__ == "__main__":
    s = server(2674, callback=handler)
    print("Waiting for connections...")
    while True:
        s.next_connection()
