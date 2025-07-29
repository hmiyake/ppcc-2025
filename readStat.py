#!/bin/env python

def readStat(filename):
    stat = {}
    with open(filename, 'r') as f:
        for line in f:
            item = line.strip()
            stats[item] = stat.get(item, 0) +1
    for key in stat:
        print (f"{key} : {stat[key]}" )

if __name__ == "__main__":
    readStat("stat.txt")
