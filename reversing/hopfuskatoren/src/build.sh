gcc -o hoppomat vm.c
strip hoppomat
python3 gen_prog.py > prog.hop
python3 assemble.py prog.hop
mv prog hopfuskeret
