#!/usr/bin/python
import random
import sys


def main(count):
    chosen = []

    while len(chosen) < count:
        r = random.randint(1, count)
        if r not in chosen:
            chosen.append(r)

    for i in range(count/2):
        pair = (chosen[i*2], chosen[i*2+1])
        print pair



if __name__ == "__main__":
    main(int(sys.argv[1]))
