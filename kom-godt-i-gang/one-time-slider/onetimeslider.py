import secrets

def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]

with open("flag.txt", "rb") as f:
    flag = list(f.read().strip())

n = len(flag)
otp = secrets.token_bytes(n)

# Slide OTP henover plaintext og XOR krypter alt, der er indenfor den
for i in range(2 * n + 1):
    flag[max(0, i - n):i] = xor(flag[max(0, i - n):i], otp[-i:])

print(bytes(flag).hex())
