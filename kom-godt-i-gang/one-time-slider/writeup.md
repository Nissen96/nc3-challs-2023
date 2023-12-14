# Writeup

Kryptonissen har hørt om One Time Pads (OTPs) og fundet på sin egen lille smarte kryptering,
der bygger ovenpå i et forsøg på et forbedre sikkerheden, men han har ikke læst godt nok op!
En OTP er en nøgle af helt tilfældige bytes, der er lige så lang som den besked, der skal krypteres.
Den må kun benyttes én gang, deraf navnet.

En OTP giver reel perfekt kryptering, men er ikke anvendlig i praksis, fordi der skal genereres en lige så lang nøgle som beskeden, den skal distribueres hemmeligt til modtageren, og den må aldrig genbruges.

Men hvad har kryptonissen gjort?
Jo, kryptonissen har genereret en OTP, og har så "slidet" den henover beskedens bytes, som her illustreret med 4 bytes (`bX` er beskedbytes og `kX` er key bytes):

```
k0 k1 k2 k3 ->
         b0 b1 b2 b3

   k0 k1 k2 k3 ->
         b0 b1 b2 b3

      k0 k1 k2 k3 ->
         b0 b1 b2 b3

         k0 k1 k2 k3 ->
         b0 b1 b2 b3

            k0 k1 k2 k3 ->
         b0 b1 b2 b3

               k0 k1 k2 k3 ->
         b0 b1 b2 b3

                  k0 k1 k2 k3 ->
         b0 b1 b2 b3
```

For hver position krypteres alle beskedbytes med en simpel XOR med den key byte, der lige nu er slidet henover.

Hvad betyder det i praksis? Jo, det betyder, at *alle* bytes i beskeden er blevet XORet med *alle* bytes i nøglen.
Det vil altså sige, at hver eneste byte i beskeden er krypteret med samme key byte, nemlig `k1 ^ k2 ^ ... ^ kN`.

Vi kan altså derfor bare prøve alle 256 mulige byte værdier som nøgle og se, om vi får noget der ligner et flag!
Eller vi kan være endnu smartere: Vi kender jo de første bytes, `NC3{`, og da `ct = pt ^ key` gælder også `key = pt ^ ct`,
så vi kan bare XOR de første 4 bytes i den krypterede tekst med `NC3{`:

```py
def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

pt = b"NC3{"
ct = bytes.fromhex("e9e494dc")

print(xor(pt, ct).hex())
```

Kører vi det, får vi output `a7a7a7a7`, dvs. vi kan som forventet se,
at alle de fire første bytes er krypteret med samme key, nemlig `a7`.

Udregner vi XOR mellem alle bytes i ciphertext og `a7` får vi flaget:

```py
flag = bytes([c ^ 0xa7 for c in ct]).decode()
print(flag)
```

Som alternativ kan et bruteforce script findes i [solve.py](solution/solve.py),
der prøver alle 256 mulige keys indtil flaget er korrekt dekrypteret.

**Flag**

`NC3{vent_var_det_dumt_at_XOR_alle_bytes_med_hver_key_byte???}`
