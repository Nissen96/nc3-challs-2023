#include <stdint.h>
#include <stdio.h>

uint32_t fnv32_hash(const char *str, size_t len) {
    /* Fowler-Noll-Vo hash function (NOT a cryptographic hash function) */
    unsigned char *s = (unsigned char *)str;

    uint32_t h = 0x811c9dc5;
    while (len--) {
        // Xor the bottom with the current octet
        h ^= *s++;

        // Multiply by the 32 bit FNV magic prime mod 2^32
        h *= 0x01000193;
    }

    return h;
}

int main() {
    char *flag = "NC3{hmm_t0_byt3s_4f_g4ng3n_v4r_n0k_f0r_l1d7}";
    for (int i = 0; i < 22; i++) {
        uint32_t hash = fnv32_hash(flag + i * 2, 2);
        printf("%u, ", hash);
    }
    puts("");

    return 0;
}
