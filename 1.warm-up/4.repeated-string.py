import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    """
    The first line contains a single string, s.
    The second line contains an integer, n.
    // (The floor division) - It rounds the result down to the nearest whole number
    % (MODULUS) - Works on integers and yields the remainder when the 1st operand is divided by the 2nd.
    """
    repeated = (s.count('a') * (n // len(s)))
    sliced_s = s[:n%len(s)].count('a')

    print(sliced_s + repeated)
    # return sliced_s + repeated

if __name__ == '__main__':
    s = input()

    n = int(input())

    repeatedString(s, n)

"""
SAMPLE INPUT 1
aba                           
10
OUTPUT
7

SAMPLE INPUT 2
a
1000000000000
OUTPUT
1000000000000
"""