import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    position = jumps = 0

    while position != len(c)-1:
        if (position +2) <= (len(c)-1) and c[position+2] != 1:
            jumps += 1
            position += 2
        else:
            jumps += 1
            position += 1

    # return jumps
    print(jumps)

if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))
 
    jumpingOnClouds(c)

"""
SAMPLE INPUT 1
6
0 0 0 0 1 0
OUTPUT
3

SAMPLE INPUT 2
7
0 0 1 0 0 1 0
OUTPUT
4
"""