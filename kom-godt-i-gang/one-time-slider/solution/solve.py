def decrypt(ct, key):
    return bytes([b ^ key for b in ct])

ct = bytes.fromhex("e9e494dcd1c2c9d3f8d1c6d5f8c3c2d3f8c3d2cad3f8c6d3f8ffe8f5f8c6cbcbc2f8c5ded3c2d4f8cac2c3f8cfd1c2d5f8ccc2def8c5ded3c2989898da")

for key in range(256):
    pt = decrypt(ct, key)
    if pt.startswith(b"NC3{"):
        print(pt.decode())
        break
