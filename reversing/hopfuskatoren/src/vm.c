#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <sys/types.h>

/***
 * Hopfuskatoren
 *
 * General idea: open code file and parse iteratively
 * Instructions = OPCODE:[OPERANDS]:OFFSET
 * Reads in OPCODE, then decode-and-fetch (possibly OPERANDS), and finally seeks OFFSET bytes cyclically
 * VM is fully stack-based with no registers, ints are 16-byte little endian, and the entry point is written in the first two bytes
 *
 * Instruction set:
 *   0: PUSH 0
 *   1: POP TOS
 *   2: TOS += 1
 *   3: TOS *= 2
 *   4: TOS1 -= TOS
 *   5: TOS1 ^= TOS
 *   6: JNZ OP1
 *   7: PUSH READ(OP1)    # read OP1 bytes from stdin and push to stack
 *   8: WRITE(POP OP1)    # pop OP1 bytes from stack and write to stdout
 *   9: PUTC(OP1)         # write char OP1 to stdout
 *  7f: EXIT
 *   _: SKIP              # unknown instructions are simply skipped
***/

int16_t read_int16(FILE* file) {
    return getc(file) | (getc(file) << 8);
}

int run(FILE* ip, long end) {
    long stack[256];
    long stackptr = 0;
    unsigned char length;
    int pos;
    int seek;
    int16_t jump;

    int entrypoint = read_int16(ip);
    fseek(ip, entrypoint, SEEK_SET);

    while (true) {
        unsigned char opcode = fgetc(ip);

        switch(opcode) {
            case 0x0:
                stack[stackptr++] = 0;
                break;
            case 0x1:
                stack[--stackptr] = 0;
                break;
            case 0x2:
                stack[stackptr - 1] += 1;
                break;
            case 0x3:
                stack[stackptr - 1] *= 2;
                break;
            case 0x4:
                stack[stackptr - 2] -= stack[stackptr - 1];
                break;
            case 0x5:
                stack[stackptr - 2] ^= stack[stackptr - 1];
                break;
            case 0x6:
                pos = ftell(ip);
                jump = read_int16(ip);
                seek = (jump + pos) % end;
                if (stack[stackptr - 1] != 0) {
                    fseek(ip, seek, SEEK_SET);
                    continue;
                }
                break;
            case 0x7:
                length = fgetc(ip);
                for (int i = 0; i < length; i++) {
                    stack[stackptr++] = fgetc(stdin);
                }
                break;
            case 0x8:
                length = fgetc(ip);
                for (int i = 0; i < length; i++) {
                    printf("%c\n", (char)stack[--stackptr]);
                }
                break;
            case 0x9:
                printf("%c", getc(ip));
                break;
            case 0x7f:
                return 0;
            default:
                fgetc(ip);
                continue;
        }

        pos = ftell(ip);
        jump = read_int16(ip);
        seek = (jump + pos) % end;  // wrap around
        fseek(ip, seek, SEEK_SET);
    }

    return 0;
}

int main(int argc, char** argv) {
    FILE *fileptr;
    char *code;

    if (argc != 2) {
        puts("Usage: vm <file>");
    }

    fileptr = fopen(argv[1], "rb");
    if (fileptr == NULL) {
        puts("Not a valid file.");
        return -1;
    }

    // Find file length and reset
    fseek(fileptr, 0L, SEEK_END);
    long length = ftell(fileptr);
    rewind(fileptr);

    run(fileptr, length);

    return 0;
}
