from Crypto.Util.number import getPrime, bytes_to_long as b2l


with open("flag.txt", "rb") as f:
    flag = f.read().strip()

p = getPrime(1024)
q = getPrime(1024)
n = p * q
phi = (p - 1) * (q - 1)

e = 0x10001
d = pow(e, -1, phi)

m = b2l(flag)
ct = pow(m, e, n)

assert m == pow(ct, d, n)

print(f"{n = }")
print(f"{q = }")
print(f"{e = }")
print(f"{ct = }")
