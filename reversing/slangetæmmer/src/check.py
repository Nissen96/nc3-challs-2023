import hashlib
from itertools import permutations


hashed = [
    "aaec1d22915a22823a4c3f7bc703c9d8b64288963c52ad775f390e349d3d79dbee26ca85c2e5037e2963d56ea6a68ec8966dcd7a8a5682aebcab816e0eb46ad43706a15b",
    "d75398281eca704576d6ee448d33ffe0e2c69023d04978b556c993d190ea19d77211bed553716a0b0f386b9f11b1d53f5d0c32b67521e341d48b08f214d1dac0738f16d0",
    "bb38e6017d41e8c1bde85bbbab328dcead86ed77ecf94b9274e7b046f10ed76903227b61da3efced1c50ec06b8bdeb26580470e43fab7a2f9df80382ef2ec5b4e78cbcce",
    "69d7904bbe2fcbb67ac9ca0c572f915ef1893ee6852d3fb20d6e18bd695bf12054ee9f6e0e942e78660cef070d4de4aad2b4ab06605446531ca5a2370658803cdf07b59f",
    "adf84935cc097254b1e6b4951083881adc3ab2091542b18094ad6a5267f981a65c22b68e7156271054bbbf64e8a8c24eb99620973452aeb4dded63a5a761aeecf54e41f8",
    "321bd46e17b382aafdf859206663bea66be3999c25cbbe04f14a1f4662049aaa57a8c54f96c82ecf47798344ed570dbee2845d7219e596a3e324281407eb5c11093c0152",
    "ecf94b9274e7b046f10ed76903227b61da3efced1c50ec06b8bdeb26580470e4bb38e6017d41e8c1bde85bbbab328dcead86ed773fab7a2f9df80382ef2ec5b4e78cbcce",
    "23006ec47629c459550c9d9508b7a41b787ee271cfc32f9fb833050e3b97395dafca0a35edf86bf00461a0708031a6f02017a1ae32fc4361d21cbddfa8a7b7717fda2e2d",
    "5d813a4760b2777d5432ecbbf7b3ad4ed93efa4655f87cebfcbbe2b72322f1a916c0b45e54160daab249b73ed721d2fe4ca6e5e4a5616963c5f06e26af18c3a96d8743ca",
    "9bd38c6328f08abef092431841c64d0507aac58bbde79f3cd21ab835fd1b61b11a36313b7ed15ba14e0acb4da569b8b7aadb472c00b42a97facc16192b7ce198eac4581d",
    "3fab7a2f9df80382ef2ec5b4e78cbccebb38e6017d41e8c1bde85bbbab328dcead86ed77ecf94b9274e7b046f10ed76903227b61da3efced1c50ec06b8bdeb26580470e4",
    "a7461302cba50be54d27370d764a3742983546b1c2212457b76a1819d17e3f2a976ff78aa8fbadcacf1355b80bc823df3d121d4b20d14684f488f6c16cf1dd4d777722b4",
    "c0ffc0791ce5ff11e12a5856d5e093d3c97dbf313fd9578e124c68aa49885b22b61b4ec8a7d084461334fa4155320e5ad7154672ee6184f673dd935d6f05829a923c4528",
    "ba8245936e64d82c81d47545c40b3197b291a653b94857f6a905ccd028329b0a8324ac4cb4b5787bdd25e10c94d1f22aae4ada7475f3a5ffe408b6d91ecf43ff372b68b6",
    "bb38e6017d41e8c1bde85bbbab328dcead86ed77ecf94b9274e7b046f10ed76903227b61da3efced1c50ec06b8bdeb26580470e43fab7a2f9df80382ef2ec5b4e78cbcce",
    "430f03c2ea70bd28108d593eca0c7c303ea8baed2791e753cb44b799c1120d02a0941f0a98faeb25e0d529f3c9f9fcec11ea6520c5dcfb1bebda52a8db275c477817a340",
    "8dd3726fb20414ce07c1be7be0bac472ab66f33034e6edb4d721a13ad4a89b3ee94656b6137dd01f26085f984afe853e5735c18587c00bcd9377de5415a65a87bf68dfe8",
    "edf86bf00461a0708031a6f02017a1ae32fc4361d21cbddfa8a7b7717fda2e2d787ee271cfc32f9fb833050e3b97395dafca0a3523006ec47629c459550c9d9508b7a41b",
    "c0148e499ba04d2c1d99021fc28cd0ba6cf9856bad46789f9ffd7e66fe565d594802dcfc9e75bf72a37d92764b19e4dd932cbd2c97c696d6c687259d83f68cff66becef5",
    "111f9d28a8427d98afcb7d1d4eb59f2abe5528eab0c950a1acbe01638c01f2527ecc92917e9c4556cc19f457ddc41af85f0f89d9fa9043335e71b1a343a280e81291a0a4",
    "23006ec47629c459550c9d9508b7a41b787ee271cfc32f9fb833050e3b97395dafca0a35edf86bf00461a0708031a6f02017a1ae32fc4361d21cbddfa8a7b7717fda2e2d",
    "98faeb25e0d529f3c9f9fcec11ea6520c5dcfb1bebda52a8db275c477817a340430f03c2ea70bd28108d593eca0c7c303ea8baed2791e753cb44b799c1120d02a0941f0a",
    "aadb472c00b42a97facc16192b7ce198eac4581d1a36313b7ed15ba14e0acb4da569b8b79bd38c6328f08abef092431841c64d0507aac58bbde79f3cd21ab835fd1b61b1",
    "ecf94b9274e7b046f10ed76903227b61da3efced1c50ec06b8bdeb26580470e43fab7a2f9df80382ef2ec5b4e78cbccebb38e6017d41e8c1bde85bbbab328dcead86ed77",
    "3fd9578e124c68aa49885b22b61b4ec8a7d084461334fa4155320e5ad7154672ee6184f673dd935d6f05829a923c4528c0ffc0791ce5ff11e12a5856d5e093d3c97dbf31",
    "d93efa4655f87cebfcbbe2b72322f1a916c0b45e54160daab249b73ed721d2fe5d813a4760b2777d5432ecbbf7b3ad4e4ca6e5e4a5616963c5f06e26af18c3a96d8743ca",
    "fc5940aadeacd5e9079c50e8dd481bbc2d549e5339e0d8293c61bb2ffe6463fafa856f73858188a4fcb95a47aa63b01da6b5053fd05592a0f1909932633ddf1026fd7b2c",
]


def check_flag(flag):
    if len(flag) != len(hashed):
        return False

    if not flag.startswith("NC3{"):
        return False

    if not flag[-1] == "}":
        return False

    for c, h in zip(flag, hashed):
        md5 = hashlib.md5(c.encode()).hexdigest()
        sha1 = hashlib.sha1(c.encode()).hexdigest()
        sha256 = hashlib.sha256(c.encode()).hexdigest()
        hashes = [md5, sha1, sha256]
        for perm in permutations(hashes):
            if "".join(perm) == h[::-1]:
                break
        else:
            return False
    return True


flag = input("Check dit flag her: ").strip()
if check_flag(flag):
    print("Sådan! Godt gået!")
else:
    print("Wah wah, prøv igen :(")
