#!/bin/bash
# Disassemble and make minor whitespace change in output to throw off automated tools
python3 -m dis check.py | sed -r "s/^ ( ?)([[:digit:]]+)/\1\2:/g" > flag_check.disSssSsS
