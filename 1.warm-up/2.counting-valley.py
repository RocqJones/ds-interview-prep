import math
import os
import random
import re
import sys

# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path

def countingValleys(steps, path):
    # Write your code here
    valley = level = 0
    u_step = 'U'
    d_step = 'D'

    for s in range(steps):
        if path[s] == u_step:
            level += 1

            if(level == 0):
                valley += 1

        elif path[s] == d_step:
            level -= 1

    # return valley
    print(valley)

if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    countingValleys(steps, path)

"""
Sample input
8
UDDDUDUU
Sample output
1
"""