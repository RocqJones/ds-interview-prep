import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    rotate = (a[d:] + a[:d])
    return rotate

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    rotLeft(a, d)

"""
SAMPLE INPUT
5 4
1 2 3 4 5
OUTPUT
5 1 2 3 4
"""