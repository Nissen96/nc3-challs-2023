#include <stdint.h>
#include <stdio.h>

uint32_t fnv32_hash(const char *str, size_t len) {
    unsigned char *s = (unsigned char *)str;

    uint32_t h = 0x811c9dc5;
    while (len--) {
        h ^= *s++;
        h *= 0x01000193;
    }
    return h;
}

int main() {
    char buf[64];
    printf("Kode, tak!\n> ");
    fgets(buf, 64, stdin);

    uint32_t hashes[] = {
        904296662, 1324349371, 1681584206, 1915632229,
        155512425, 1292594660, 1197446016, 1190128419,
        2601248942, 841129138, 186654902, 1513513826,
        1106240324, 1493926088, 1206067395, 1091263232,
        1189981324, 1225484184, 1609421799, 1124818470,
        1743495656, 1424323537
    };

    for (int i = 0; i < 22; i++) {
        if (fnv32_hash(buf + i * 2, 2) != hashes[i]) {
            puts("Smut!");
            return 0;
        }
    }
    puts("Hurraaa, velkommen ind!");

    return 0;
}
