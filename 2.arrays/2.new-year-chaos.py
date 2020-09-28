import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    num_moves = 0
    for x in range(n - 1, -1, -1):
        if (q[x] - (x + 1)) > 2:
            print("Too chaotic")
            return

        for y in range(max(0, q[x] - 2), x, 1):
            if q[y] > q[x]:
                num_moves += 1

    print(num_moves)
    # return num_moves

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

"""
SAMPLE INPUT
2
5
2 1 5 3 4
5
2 5 1 3 4
OUTPUT
3
Too chaotic
"""