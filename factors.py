#!/usr/bin/env python3
import sys
import math

def facto_rise(no):
    for i in range(2, math.isqrt(no) + 1):
        if no % i == 0:
            return i, no // i
    return no, 1

def main():
    with open(sys.argv[1], 'r') as file:
        for line in file:
            no = int(line.strip())
            p, q = facto_rise(no)
            print(f"{no}={p}*{q}")

if __name__ == "__main__":
    main
   