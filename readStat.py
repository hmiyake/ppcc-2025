#!/bin/env python

import sys

def readStat(filename):
    stat = {}
    ratio = []
    maxItem = ['None', 0]
    minItem = ['None', sys.maxsize]

    with open(filename, 'r') as f:
        for line in f:
            item = line.strip()
            stat[item] = stat,get(item, 0) +1

    total = sum([stat[k] for k in stat])
    for key in stat:
        ratio[key] = float(stat[key])/float(total)
        bar = '*' * int(stat[key])
        if int(stat[key]) > maxItem[1]:
        maxItem = [key, stat[key]]
        if int(stat[key]) < minItem[1]:
            minItem = [key, stat[key]]
        print (f"{key}:\t{stat[key]} ({ratio[key]*100:.1f}%) {bar}" )

    print (f'\nLargest item: {maxItem[1]} ({maxItem[0]})')
    print (f'Smallest item: {minItem[1]} ({minItem[0]})')

if __name__ == "__main__":
    readStat("stat.txt")
